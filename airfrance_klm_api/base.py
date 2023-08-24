import os
import requests

class AirfranceKLM:
    """
    Base class to be inherited by the various subclasses
    in this package. This class provides the basic 
    abilities to connect to the Airfrance KLM Developer
    API.

    Args:
        api_key : str
            Airfrance KLM API Key created in their developer 
            portal.
        api_secret : str
            Airfrance KLM API Secret created in their 
            developer portal.
    
    Returns:
        AirfranceKLM : AirfranceKLM
    """

    def __init__(self, api_key: str, api_secret: str):

        self.api_key: str = api_key
        self.api_secret: str = api_secret

    def _make_request(self):
        """
        Helper method to generate requests using the 
        `requests` library. Retry logic is built in
        for convenience.
        """

