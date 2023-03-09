import requests
import os
from requests.exceptions import RequestException
from requests.adapters import HTTPAdapter


class HostService:
    """Implements host discovery capabilities"""

    @staticmethod
    def is_running_in_the_cloud(app):
        """
        :return: Whether we are running in EC2 by checking if there's connectivity to the IP address
        """

        # Just verifying if the config value has been checked before, if so just return the status
        if not app.config['IN_CLOUD'] is None:
            return app.config['IN_CLOUD']["status"]

        # As the server is bootstrapping, then just consider it's not
        app.config['IN_CLOUD'] = {
            "status": False,
            "metadata": {},
            "type": "local"
        }
        try:
            # We create a requests.Session() object and mount an HTTPAdapter() object with a max_retries value of 0.
            # This ensures that the requests.get() function will not retry in case of a connection error or a timeout.
            session = requests.Session()
            # https://stackoverflow.com/questions/15431044/can-i-set-max-retries-for-requests-request/15431343#15431343
            retries = HTTPAdapter(max_retries=1)
            session.mount('http://', retries)

            # Making sure we timeout very quickly for the single request
            # https://requests.readthedocs.io/en/stable/user/advanced/#timeouts
            # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
            response = session.get('http://169.254.169.254/latest/meta-data/', timeout=1)
            app.config['IN_CLOUD']["status"] = response.status_code == 200
            app.config['IN_CLOUD']["type"] = "ec2" if response.status_code == 200 else "compute"
            app.logger.info("Running in the Cloud...")

        except (RequestException, TimeoutError, ConnectionError):
            app.logger.info("Not running in the Cloud...")

        # Just return the cached value
        return app.config['IN_CLOUD']["status"]

    @staticmethod
    def get_hostname(app):
        """
        :return: the hostname where the app is running: from EC2 is the public host or os hostname otherwise
        """
        # just make sure we have if we are on EC2 to show the public host for completeness
        if HostService.is_running_in_the_cloud(app):
            # Just get the public hostname from the metadata
            # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
            return requests.get('http://169.254.169.254/latest/meta-data/public-hostname').text

        # By default, just return the nodename
        # https://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname/49610911#49610911
        return os.uname().nodename
