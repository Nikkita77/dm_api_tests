from api_mailhog.apis.mailhog_api import Mailhogapi
from restclient.configuration import Configuration


class MailHogApi:
    def __init__(
            self,
            configuration: Configuration
            ):
        self.configuration = configuration
        self.mailhog_api = Mailhogapi(configuration=self.configuration)
