# https://stackoverflow.com/questions/18214612/how-to-access-app-config-in-a-blueprint/38262792#38262792
from flask import Blueprint, current_app as app

import os
import boto3
import json

from viasat.platform.cloud.host_service import HostService

healthcheck_api = Blueprint('healthcheck_api', __name__, url_prefix='/healthcheck')


@healthcheck_api.route('/liveness')
def admin_liveness_healthcheck():
    """
    :return: Show-casing plain text HTTP response for single liveliness, or liveness, health check
    """
    app.logger.info("App successfully listening on port ")
    return "Ok", 200, {'content-type': 'text/plain'}


@healthcheck_api.route('/readiness')
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
            "resource": app.config["LOCAL_DATABASE_URL"],
            "status": None,
        }
    }

    # Just whether the database is initialized locally or through external service (RDS)

    if not HostService.is_running_in_the_cloud(app):
        # Just checking if the file exists...
        db_file_path = app.config["LOCAL_DATABASE_URL"].replace("sqlite:///", "")
        status = 200 if os.path.isfile(db_file_path) else 503
        readiness_check["database"]["status"] = status
        readiness_check["overall"] = status

    else:
        # Fix https://stackoverflow.com/questions/40377662/boto3-client-noregionerror-you-must-specify-a-region-error-only-sometimes/56131018#56131018
        # raise NoRegionError() botocore.exceptions.NoRegionError: You must specify a region
        # As the in cloud config has the metadata, we can use the default region where the apps is running
        os.environ['AWS_DEFAULT_REGION'] = app.config["IN_CLOUD"]["metadata"]["region"]

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

