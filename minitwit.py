﻿# -*- coding: utf-8 -*-
"""
    MiniTwit
    ~~~~~~~~

    A microblogging application written with Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
import time

from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect
from flask import render_template, abort, g, flash
from flask_cli import FlaskCLI
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as db
from sqlalchemy.sql import text

# configuration

# By default, use a local sqlite db
DB_TYPE = 'sqlite'
DATABASE_URL = DB_TYPE + ':////var/minitwit/minitwit.db'

SCHEMAS = dict(
    sqlite='db_sqlite.sql',
    mysql='db_mysql.sql',
    )

PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

DB_STASH = 'db'
DB_PASSWORD_FILE = '/etc/minitwit.password'


# create our little application :)
app = Flask(__name__) #pylint: disable=invalid-name
FlaskCLI(app)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)


def get_db_password():
    ''' Try to get our db password from a file.
        Otherwise get it from our config.
    '''
    db_password_file = app.config.get('DB_PASSWORD_FILE')

    return (
        open(db_password_file, 'r').read() if os.path.isfile(db_password_file)
        else app.config.get('DB_PASSWORD'))


def make_db_engine():
    ''' Figure what database we're using and create a engine for it
    '''
    db_type = app.config.get('DB_TYPE')

    if db_type == DB_TYPE:
        db_url = DATABASE_URL
    else:
        db_url = '{}://{}:{}@{}:3306/{}'.format(
            db_type,
            app.config.get('DB_USER'),
            get_db_password(),
            app.config.get('DB_ENDPOINT'),
            app.config.get('DB_NAME'))

    print('db url is:', db_url)
    return db.create_engine(db_url)


DB_ENGINE = make_db_engine()


def get_db():
    """Opens a new database connection if there is none yet for the
    current request.
    """
    if DB_STASH not in g:
        g.db = DB_ENGINE.connect()

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
    schema_file = SCHEMAS[app.config['DB_TYPE']]

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
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = :userid',
                          {'userid': session['user_id']}, one=True)


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
        {'userid': session['user_id'], 'whoid': session['user_id'], 'limit': PER_PAGE}))


@app.route('/public')
def public_timeline():
    """Displays the latest messages of all users."""
    return render_template('timeline.html', messages=query_db('''
        select message.*, user.* from message, user
        where message.author_id = user.user_id
        order by message.pub_date desc limit :limit''', {'limit': PER_PAGE}))


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
        profile_user=profile_user)


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


# add some filters to jinja
#pylint: disable=no-member
app.jinja_env.filters['datetimeformat'] = format_datetime
app.jinja_env.filters['gravatar'] = gravatar_url
#pylint: enable=no-member
