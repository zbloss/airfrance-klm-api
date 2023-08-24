import os
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import JSONDecodeError
from requests.packages.urllib3.util.retry import Retry


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
        base_url : str
            Base URL to prepend to endpoints pass in
            `self._make_request`.

    Returns:
        AirfranceKLM : AirfranceKLM
    """

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = "https://live.airfranceklm.com",
    ):
        self.api_key: str = api_key
        self.api_secret: str = api_secret
        self.headers: dict = {
            "API-Key": self.api_key,
            "Content-Type": "application/json",
        }

        self.base_url = base_url

    def _make_request(
        self,
        endpoint: str,
        data: dict = Optional[None],
        post_call: bool = True,
        max_retries: int = 5,
        backoff_factor: int = 3,
        retry_on_status_codes: list = [400, 404, 423, 429, 500, 502, 503, 504],
    ):
        """
        Helper method to generate requests using the
        `requests` library. Retry logic is built in
        for convenience.

        Args:
            endpoint : str
                API endpoint to make an API call to.
            data : dict
                Optional dictionary payload to send in the
                API call.
                [Optional] default: None.
            post_call : bool
                True if you want to make a POST request else a
                GET request is made instead.
                [Optional] default: True.
            max_retries : int
                Maximum number of times to retry the API call.
                [Optional] default: 5.
            backoff_factor : int
                Exponential scaling factor representing the number of
                seconds to wait before retrying the API call.
                [Optional] default: 3.
            retry_on_status_codes : list
                List of integer status codes on range [100, 600) to
                retry API Requests on.
                [Optional] default: [
                    400, 404, 423, 429, 500, 502, 503, 504
                ].

        Returns:
            response : dict
                Dictionary object containing the response
                from the API call.

        Raises:
            AssertionError : If retry_on_status_codes value is an invalid HTTP
                             status code.
                             :href: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
            HTTPError : If there is still an non-successful HTTP Status Code after
                        the number of retries has exceeded.

        """

        for status_code in retry_on_status_codes:
            assert (
                status_code < 599
            ), f"Status Codes must be between 100 and 599: {status_code}"
            assert (
                status_code >= 100
            ), f"Status Codes must be between 100 and 599: {status_code}"

        http_session = requests.Session()
        retries = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=retry_on_status_codes,
        )

        http_session.mount("http://", HTTPAdapter(max_retries=retries))
        http_session.mount("https://", HTTPAdapter(max_retries=retries))

        endpoint = endpoint if not endpoint.startswith("/") else endpoint[1:]
        url = f"{self.base_url}/{endpoint}"

        args = {"url": url, "headers": self.headers}
        if data is not None:
            args["data"] = data

        if post_call:
            response = http_session.post(**args)
        else:
            response = http_session.get(**args)
        response.raise_for_status()

        try:
            response = response.json()
        except JSONDecodeError as e:
            response = {"content": response.content}

        return response
