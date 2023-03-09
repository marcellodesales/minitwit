# https://stackoverflow.com/questions/18214612/how-to-access-app-config-in-a-blueprint/38262792#38262792
from flask import Blueprint, current_app as app
import os
import json

admin_api = Blueprint('admin_api', __name__, url_prefix='/admin')

from viasat.platform.core.http_auth_basic import auth
from viasat.platform.cloud.config_service import ConfigService

@admin_api.route('/env')
@auth.login_required
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


@admin_api.route('/config')
@auth.login_required
def admin_config():
    """
    :return: Show the current configuration resolved by the app
    """

    # Convert the dictionary to a JSON string, using the default str serializer
    config_json = json.dumps(app.config, default=str)

    # Obfuscate passwords
    output_obj = json.loads(config_json)
    output_obj = {k: (v[0:2] + "*****" + v[-2:] if "PASSWORD" in k else v) for k, v in output_obj.items()}

    config_json = json.dumps(output_obj, default=str)
    app.logger.info("Current config=%s", config_json)

    return config_json, 200, {'content-type':'application/json'}


@admin_api.route('/endpoints')
@auth.login_required
def admin_endpoints():
    """
    :return: Show the current configuration resolved by the app
    """

    # So we know the available endpoints to be able to call
    endpoints = ConfigService.get_current_endpoints(app)
    endpoints_json = json.dumps(endpoints, default=str)

    return endpoints_json, 200, {'content-type':'application/json'}