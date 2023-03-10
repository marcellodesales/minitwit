import requests
import os
from requests.exceptions import RequestException
from requests.adapters import HTTPAdapter


class HostService:
    """Implements host discovery capabilities"""

    @staticmethod
    def __make_single_request(url):
        session = requests.Session()
        # https://stackoverflow.com/questions/15431044/can-i-set-max-retries-for-requests-request/15431343#15431343
        retries = HTTPAdapter(max_retries=1)
        session.mount('http://', retries)

        # Making sure we timeout very quickly for the single request
        # https://requests.readthedocs.io/en/stable/user/advanced/#timeouts
        # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
        response = session.get(url, timeout=1)
        return response


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
            response = HostService.__make_single_request('http://169.254.169.254/latest/meta-data/')
            app.config['IN_CLOUD']["status"] = response.status_code == 200
            app.config['IN_CLOUD']["type"] = "ec2" if response.status_code == 200 else "compute"
            app.logger.info("Running in the Cloud...")

        except (RequestException, TimeoutError, ConnectionError):
            # Just to repeat the metadata section
            app.config['IN_CLOUD']["metadata"]: {}

        # Just return the cached value
        return app.config['IN_CLOUD']["status"]


    @staticmethod
    def get_hostname(app):
        """
        :return: the hostname where the app is running: from EC2 is the public host or os hostname otherwise
        """
        # just make sure we have if we are on EC2 to show the public host for completeness
        if not HostService.is_running_in_the_cloud(app):
            # By default, just return the nodename
            # https://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname/49610911#49610911
            return os.uname().nodename.strip()

        # Just get the public hostname from the metadata
        # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
        hostname = ""

        # Start by digging the public URL. The code was initially failing when moving the app
        # From the public to the private zone. The http response returned a 404 http error, resolved into a multi-space
        # The exception was from setting this hostname to the HTTP response header
        # "ValueError: Detected newline in header value.  This is a potential security problem"
        aws_api_url = "http://169.254.169.254/latest/meta-data"
        response = HostService.__make_single_request(aws_api_url + '/public-hostname')
        if response.status_code == 200:
            hostname = response.text
            app.logger.info("We are running at the public zone at %s", hostname)

        # If not, let's try the private, as chances are we are here...
        response = HostService.__make_single_request(aws_api_url + '/local-hostname')
        if response.status_code == 200:
            hostname = response.text
            app.logger.info("We are running at the private zone at %s", hostname)

        else:
            hostname = os.uname().nodename
            app.logger.info("Can't determine the hostname for the app... getting local hostname %s", hostname)

        # Return the value computed in the public
        hostname = hostname.strip()
        if len(hostname) == 0:
            app.logger.warning("Can't determine the hostname. Setting as undetermined!")
            hostname = "unknown"

        return hostname