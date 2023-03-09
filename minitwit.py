﻿# -*- coding: utf-8 -*-
"""
    MiniTwit
    ~~~~~~~~

    A microblogging application written with Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from collections import namedtuple
import time
import json
import os

from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect
from flask import render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as db
from sqlalchemy.sql import text
import requests
import boto3
import botocore

from viasat.platform.cloud.host_service import HostService
from viasat.platform.cloud.config_service import ConfigService
from viasat.platform.cloud.http_response_decorator import HttpResponseDecorator

# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
from viasat.platform.observability.healthcheck_routes import healthcheck_api
from viasat.platform.observability.admin_routes import admin_api

#======================================================================
# Database settings

DB_TYPE_SQLITE = 'sqlite'
DB_TYPE_MYSQL = 'mysql'

# By default, use a local sqlite db.
LOCAL_DB_TYPE = DB_TYPE_SQLITE

LOCAL_DATABASE_URL = LOCAL_DB_TYPE + ':////var/minitwit/minitwit.db'

# Schema files used to initialize the database
#
SCHEMAS = {
    DB_TYPE_SQLITE: 'db_sqlite.sql',
    DB_TYPE_MYSQL: 'db_mysql.sql',
}

#======================================================================
# configuration

CONFIG_DB_TYPE = 'DB_TYPE' # Either DB_TYPE_SQLITE (the default) or DB_TYPE_MYSQL

# The following params are used only for DB_TYPE_MYSQL

# These params must be defined
CONFIG_DB_ENDPOINT = 'DB_ENDPOINT'  # The RDS DNS name
CONFIG_DB_NAME = 'DB_NAME'          # The database name

# If DB_SECRET_ARN is defined, the program obtains the username
# and password from the specified secret stored in the AWS Secrets
# Manager.
#
CONFIG_DB_SECRET_ARN = 'DB_SECRET_ARN'
CONFIG_DB_SECRET_KEY_USERNAME = 'DB_SECRET_KEY_USERNAME'
CONFIG_DB_SECRET_KEY_PASSWORD = 'DB_SECRET_KEY_PASSWORD'

# The friendly secret name to use if no secret ARN is defined
SECRET_FRIENDLY_NAME = 'mtdb-credentials'

# Default values for the DB credentials keys
SECRET_USERNAME = 'username'
SECRET_PASSWORD = 'password'

# If DB_SECRET_ARN is not defined, the DB_USER and DB_PASSWORD params
# must be defined.
#
CONFIG_DB_USER = 'DB_USER'
CONFIG_DB_PASSWORD = 'DB_PASSWORD'

#======================================================================
# other constants

PER_PAGE = 30
DEBUG = True

# The key used to encrypt session keys
SECRET_KEY = 'development key'

DB_STASH = 'db'


#======================================================================
# create our little application :)

app = Flask(__name__) #pylint: disable=invalid-name

#The only local config param we actually read is DEBUG
app.config.from_object(__name__)

#Read config settings from the file specified by this env var, if it is defined.
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)

# Just add an extra config to see if it's in the cloud
app.config['IN_CLOUD'] = None
app.config["LOCAL_DATABASE_URL"] = LOCAL_DB_TYPE + ':////var/minitwit/minitwit.db'

# Just bootstrap the logs as soon as it loads, as other methods may need cloud metadata
ConfigService.bootstrap_cloud_metadata(app)

def get_db_credentials():
    ''' If we are configured to do so, retrieve the db username and password
        from the secrets manager. Otherwise get them from the local config.
    '''
    secret_arn = app.config.get(CONFIG_DB_SECRET_ARN)
    app.logger.info('%s=%s', CONFIG_DB_SECRET_ARN, secret_arn) #pylint: disable=no-member

    # just making sure it's in AWS
    region = "" if not is_running_in_the_cloud() else app.config['IN_CLOUD']["metadata"]["region"]

    try:
        client = boto3.client(
            'secretsmanager',
            config=botocore.client.Config(
                region_name=region,
                connect_timeout=5,
                read_timeout=5,
                retries=dict(total_max_attempts=2)))

        secret_value = json.loads(
            client.get_secret_value(SecretId=secret_arn or SECRET_FRIENDLY_NAME)['SecretString'])

        username = secret_value[app.config.get(CONFIG_DB_SECRET_KEY_USERNAME) or SECRET_USERNAME]
        password = secret_value[app.config.get(CONFIG_DB_SECRET_KEY_PASSWORD) or SECRET_PASSWORD]
        secrets_used = True

    except Exception as err: #pylint: disable=broad-except
        app.logger.info( #pylint: disable=no-member
            'Unable to get credentials from secrets manager. Using stored credentials: %s',
            str(err))
        username = app.config.get(CONFIG_DB_USER)
        password = app.config.get(CONFIG_DB_PASSWORD)
        secrets_used = False

    return namedtuple('DbCredentials', 'username password secrets_used')(
        username, password, secrets_used)


def make_db_engine():
    ''' Figure what database we're using and create a engine for it
    '''
    db_type = app.config.get(CONFIG_DB_TYPE, LOCAL_DB_TYPE)

    if db_type == LOCAL_DB_TYPE:
        db_url = LOCAL_DATABASE_URL
        app.logger.info('Using local db %s', db_url) #pylint: disable=no-member
        secrets_used = False

    else:
        endpoint = app.config.get(CONFIG_DB_ENDPOINT)
        name = app.config.get(CONFIG_DB_NAME)
        credentials = get_db_credentials()
        secrets_used = credentials.secrets_used

        db_url = '{}://{}:{}@{}:3306/{}'.format(
            db_type, credentials.username, credentials.password, endpoint, name)

        app.logger.info( #pylint: disable=no-member
            'db_type=%s endpoint=%s db=%s username=%s using_secret=%s',
            db_type, endpoint, name, credentials.username,  str(secrets_used))

    return (db.create_engine(db_url), secrets_used)


DB_ENGINE, SECRETS_USED = make_db_engine()


def get_db():
    """Opens a new database connection if there is none yet for the
    current request.
    """
    if DB_STASH not in g:
        g.db = DB_ENGINE.connect() #pylint: disable=assigning-non-slot

    return g.db


@app.teardown_appcontext
def close_database(_exception):
    """Closes the database again at the end of the request."""
    the_db = g.pop(DB_STASH, None)

    if the_db is not None:
        the_db.close()


def init_db():
    """Initializes the database."""
    the_db = get_db()

    # Use the dbtype: prefix to choose the schema.
    schema_file = SCHEMAS[app.config.get(CONFIG_DB_TYPE, LOCAL_DB_TYPE)]

    with app.open_resource(schema_file, mode='r') as fil:
        queries_string = fil.read()
        queries = queries_string.split(';')
        for query in queries:
            if len(query.strip()) > 0:
                the_db.execute(query.strip() + ';')

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def query_db(query, args=None, one=False):
    """Queries the database and returns a list of dictionaries."""

    values = list(exec_db(query, args))
    return (values[0] if values else None) if one else values


def exec_db(query, args=None):
    """Queries the database and return the result as is."""

    if args is None:
        args = dict()

    stmt = text(query)
    return get_db().execute(stmt, **args)


def get_user_id(username):
    """Convenience method to look up the id for a username."""
    value = query_db('select user_id from user where username = :username',
                     {'username': username}, one=True)
    return value[0] if value else None  #pylint: disable=unsubscriptable-object


def format_datetime(timestamp):
    """Format a timestamp for display."""
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')


def gravatar_url(email, size=80):
    """Return the gravatar image for the given email address."""
    return 'https://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
        (md5(email.strip().lower().encode('utf-8')).hexdigest(), size)


@app.before_request
def before_request():
    """ Do before-request operations """
    g.user = None #pylint: disable=assigning-non-slot
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = :userid', #pylint: disable=assigning-non-slot
                          {'userid': session['user_id']}, one=True)


# https://stackoverflow.com/questions/25860304/how-do-i-set-response-headers-in-flask/59676071#59676071
@app.after_request
def add_header(response):
    response.headers['Host'] = app.config['HOSTNAME']
    if app.config['IN_CLOUD']["status"]:
        response.headers['X-Host-AZ'] = app.config['IN_CLOUD']["metadata"]["availabilityZone"]

    # When deployed, Ansible will create the following properties:
    # BUILD_GIT_VERSION = SHA version, BUILD_GIT_REPO, BUILD_GIT_BRANCH
    app.logger.info(type(app.config))
    if app.config.get("BUILD_GIT_VERSION") is not None:
        response.headers['X-App-Version'] = str(app.config.get("BUILD_GIT_VERSION")[0:7])

    return response


@app.route('/')
def timeline():
    """Shows a users timeline or if no user is logged in it will
    redirect to the public timeline.  This timeline shows the user's
    messages as well as all the messages of followed users.
    """
    if not g.user:
        return redirect(url_for('public_timeline'))
    return render_template('timeline.html', messages=query_db(
        '''
        select message.*, user.* from message, user
        where message.author_id = user.user_id and (
            user.user_id = :userid or
            user.user_id in (select whom_id from follower
                                    where who_id = :whoid))
        order by message.pub_date desc limit :limit''',
        {'userid': session['user_id'], 'whoid': session['user_id'], 'limit': PER_PAGE}),
        secrets_used=SECRETS_USED)


@app.route('/public')
def public_timeline():
    """Displays the latest messages of all users."""
    return render_template('timeline.html', messages=query_db('''
        select message.*, user.* from message, user
        where message.author_id = user.user_id
        order by message.pub_date desc limit :limit''', {'limit': PER_PAGE}),
        secrets_used=SECRETS_USED)


@app.route('/<username>')
def user_timeline(username):
    """Display's a users tweets."""
    profile_user = query_db('select * from user where username = :username',
                            {'username': username}, one=True)
    if profile_user is None:
        abort(404)
    followed = False
    if g.user:
        followed = query_db(
            '''select 1 from follower where
            follower.who_id = :whoid and follower.whom_id = :whomid''',
            {'whoid': session['user_id'], 'whomid': profile_user['user_id']},  #pylint: disable=unsubscriptable-object
            one=True) is not None
    return render_template(
        'timeline.html',
        messages=query_db(
            '''select message.*, user.* from message, user where
            user.user_id = message.author_id and user.user_id = :userid
            order by message.pub_date desc limit :limit''',
            {'userid': profile_user['user_id'], 'limit': PER_PAGE}),  #pylint: disable=unsubscriptable-object
        followed=followed,
        profile_user=profile_user,
        secrets_used=SECRETS_USED)


@app.route('/<username>/follow')
def follow_user(username):
    """Adds the current user as follower of the given user."""
    if not g.user:
        abort(401)
    whom_id = get_user_id(username)
    if whom_id is None:
        abort(404)

    exec_db(
        'insert into follower (who_id, whom_id) values (:whoid, :whomid)',
        dict(whoid=session['user_id'], whomid=whom_id))
    # db.commit()
    flash('You are now following "%s"' % username)
    return redirect(url_for('user_timeline', username=username))


@app.route('/<username>/unfollow')
def unfollow_user(username):
    """Removes the current user as follower of the given user."""
    if not g.user:
        abort(401)
    whom_id = get_user_id(username)
    if whom_id is None:
        abort(404)

    exec_db(
        'delete from follower where who_id=:whoid and whom_id=:whomid',
        dict(whoid=session['user_id'], whomid=whom_id))

    flash('You are no longer following "%s"' % username)
    return redirect(url_for('user_timeline', username=username))


@app.route('/add_message', methods=['POST'])
def add_message():
    """Registers a new message for the user."""
    if 'user_id' not in session:
        abort(401)
    if request.form['text']:
        exec_db(
            '''insert into message (author_id, text, pub_date)
            values (:authorid, :text, :pubdate)''',
            dict(
                authorid=session['user_id'],
                text=request.form['text'],
                pubdate=int(time.time())))

        flash('Your message was recorded')
    return redirect(url_for('timeline'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for('timeline'))
    error = None
    if request.method == 'POST':
        user = query_db('''select * from user where
            username = :username''', {'username': request.form['username']}, one=True)
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['pw_hash'],  #pylint: disable=unsubscriptable-object
                                     request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['user_id']  #pylint: disable=unsubscriptable-object
            return redirect(url_for('timeline'))
    return render_template('login.html', error=error)


@app.route('/admin/env')
def admin_env():
    """
    :return: Show-casing plain text HTTP response for single liveliness, or liveness, health check
    """
    # Get the env vars as dict
    env_key_values = dict(os.environ)

    # Convert the dictionary to a JSON string
    env_json = json.dumps(env_key_values)
    app.logger.info("Current envs %s", env_json)

    return env_json, 200, {'content-type':'application/json'}


@app.route('/admin/config')
def admin_config():
    """
    :return: Show the current configuration resolved by the app
    """

    # Convert the dictionary to a JSON string, using the default str serializer
    config_json = json.dumps(app.config, default=str)
    app.logger.info("Current config=%s", config_json)

    return config_json, 200, {'content-type':'application/json'}


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    if g.user:
        return redirect(url_for('timeline'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or \
                '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            exec_db(
                '''insert into user (
                username, email, pw_hash) values (:username, :email, :pwhash)''',
                dict(
                    username=request.form['username'],
                    email=request.form['email'],
                    pwhash=generate_password_hash(request.form['password'])))

            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    """Logs the user out."""
    flash('You were logged out')
    session.pop('user_id', None)
    return redirect(url_for('public_timeline'))


@app.route('/admin/health/liveness')
def admin_liveness_healthcheck():
    """
    :return: Show-casing plain text HTTP response for single liveliness, or liveness, health check
    """
    app.logger.info("App successfully listening on port ")
    return "Ok", 200, {'content-type': 'text/plain'}


@app.route('/admin/health/readiness')
def admin_readiness_healthcheck():
    """
    :return: The readiness probe that verifies and gets the status of the app with a deep health check to RDS.
    NOTE: This is for demonstrations purposes only!
    """

    # the server at this point is always 200, but the overall will be 503 depending on RDS
    readiness_check = {
        "overall": 503,
        "server": 200,
        "database": {
            "type": "sqlite",
            "resource": LOCAL_DATABASE_URL,
            "status": None,
        }
    }

    # Just whether the database is initialized locally or through external service (RDS)

    if not is_running_in_the_cloud():
        # Just checking if the file exists...
        db_file_path = LOCAL_DATABASE_URL.replace("sqlite:///", "")
        status = 200 if os.path.isfile(db_file_path) else 503
        readiness_check["database"]["status"] = status
        readiness_check["overall"] = status

    else:
        # Create an RDS client
        rds = boto3.client('rds')

        # Call the describe_db_instances method to get information about all RDS instances
        response = rds.describe_db_instances()

        # Loop through the DBInstances and find the instance with the specified endpoint
        db_instance_status = None
        for db_instance in response['DBInstances']:
            if db_instance['Endpoint']['Address'] == app.config.get(CONFIG_DB_ENDPOINT):
                # Extract the DB instance status from the response
                db_instance_status = response['DBInstances'][0]['DBInstanceStatus']
                break

        # Check if the DB instance is available
        readiness_check["database"]["type"] = "rds"
        readiness_check["database"]["status"] = 200 if db_instance_status == 'available' else 503
        readiness_check["database"]["resource"] = app.config.get(CONFIG_DB_ENDPOINT)
        readiness_check["overall"] = readiness_check["database"]["status"]

    # TODO: verify if the schema is initialized before returning

    # Just log
    response_json = json.dumps(readiness_check, indent=4)
    if readiness_check["database"]["status"] == 503:
        app.logger.warning("The database '%s' is not ready! status must be 'available': readiness_check=%s",
                        readiness_check["database"]["type"], response_json)
    else:
        app.logger.info("The database '%s' is fully ready! readiness_check=%s",
                        readiness_check["database"]["type"], response_json)

    # https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask/54361534#54361534
    # https://stackoverflow.com/questions/11773348/python-flask-how-to-set-content-type/24852564#24852564
    return json.dumps(readiness_check), readiness_check["overall"], {'content-type':'application/json'}


# add some filters to jinja
#pylint: disable=no-member
app.jinja_env.filters['datetimeformat'] = format_datetime
app.jinja_env.filters['gravatar'] = gravatar_url
#pylint: enable=no-member

if __name__ == '__main__':
    # Model: https://gist.github.com/rtzll/8f0f7668c4ca9813e9380b45b932e7c2
    # https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
    app.register_blueprint(healthcheck_api)
    app.register_blueprint(admin_api)

    # So we know the available endpoints to be able to call
    ConfigService.log_available_endpoints(app)

    # flask run --host=0.0.0.0 --with-threads --no-debugger --no-reload
    server = app.run(host='0.0.0.0', threaded=True, debug=False, use_reloader=False)
