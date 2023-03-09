import json
import os
import requests

from viasat.platform.cloud.host_service import HostService


class ConfigService:
    """Implements host discovery capabilities"""

    @staticmethod
    def __log_current_environment(app):
        # Just log the current env as bootstrap record
        env_key_values = "\n"
        for k, v in os.environ.items():
            env_key_values += f'{k}={v}' + "\n"
        app.logger.info("Current environment: %s", env_key_values)


    @staticmethod
    def log_current_config(app):
        # Just make sure to use the string parser when dumping to string to avoid serialization issues
        # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844
        app.logger.info("Loaded with the following config: %s",
                        json.dumps(app.config, indent=4, sort_keys=True, default=str))


    @staticmethod
    def bootstrap_cloud_metadata(app):
        """
        Loads the metadata about the service just for information, printing the env info
        """
        ConfigService.__log_current_environment(app)

        app.logger.info("Bootstrapping app server...")

        # Fetch the first information, which will force to check the cloud
        app.config['HOSTNAME'] = HostService.get_hostname(app)

        if not HostService.is_running_in_the_cloud(app):
            app.logger.warning("Can't fetch the cloud metadata because this instance is not in the cloud!")
            ConfigService.log_current_config(app)
            return

        # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
        cloud_metadata = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document').text
        app.config['IN_CLOUD']["metadata"] = json.loads(cloud_metadata)

        ConfigService.log_current_config(app)


    @staticmethod
    def get_current_endpoints(app):
        # https://stackoverflow.com/questions/30081802/flask-blueprints-list-routes/52065090#52065090
        registered_endpoints = [str(p) for p in app.url_map.iter_rules()]
        return registered_endpoints


    @staticmethod
    def log_available_endpoints(app):
        # https://stackoverflow.com/questions/30081802/flask-blueprints-list-routes/52065090#52065090
        registered_endpoints = ConfigService.get_current_endpoints(app)
        app.logger.info("Endpoints: %s", str(registered_endpoints))
