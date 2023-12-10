import os

import pytest
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from airfrance_klm_api.base import AirfranceKLM
from airfrance_klm_api.models.config import Config


class TestBase:
    api_key: str = "hey"
    api_secret: str = "there"
    base_url: str = "https://live.airfranceklm.com"
    default_config: Config = Config(API_KEY=api_key, API_SECRET=api_secret)
    airfranceklm = AirfranceKLM(config=default_config)


    def test___init__(self):
        assert isinstance(self.airfranceklm.config.API_KEY, str)
        assert isinstance(self.airfranceklm.config.API_SECRET, str)
        assert isinstance(self.airfranceklm.config.headers, dict)

        assert self.airfranceklm.config.headers["API-Key"] == self.api_key
        assert self.airfranceklm.config.headers["Content-Type"] == "application/json"

    @pytest.mark.integration_test
    def test__make_request(self):
        with pytest.raises(HTTPError):
            self.airfranceklm._make_request(
                endpoint="/mega-invalid-endpoint-fa-sho", data=None
            )
