

class HttpResponseDecorator:
    """Implements host discovery capabilities"""

    @staticmethod
    def decorate_with_host_info(app, response):
        response.headers['Host'] = app.config['HOSTNAME']
        if app.config['IN_CLOUD']["status"]:
            response.headers['X-Host-AZ'] = app.config['IN_CLOUD']["metadata"]["availabilityZone"]

    @staticmethod
    def decorate_with_app_info(app, response):
        # When deployed, Ansible will create the following properties:
        # BUILD_GIT_VERSION = SHA version, BUILD_GIT_REPO, BUILD_GIT_BRANCH
        if app.config.get("BUILD_GIT_VERSION") is not None:
            # Define the first 7 characters from Git SHA, as it is short and yet addressable by github
            response.headers['X-App-Version'] = str(app.config.get("BUILD_GIT_VERSION")[0:7])