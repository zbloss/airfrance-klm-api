import os

import pytest
from dotenv import load_dotenv
from requests.exceptions import HTTPError 
from airfrance_klm_api.base import AirfranceKLM

load_dotenv()


class TestBase:
    AF_KLM_API_KEY = os.getenv("AF_KLM_API_KEY")
    AF_KLM_API_SECRET = os.getenv("AF_KLM_API_SECRET")

    airfranceklm = AirfranceKLM(AF_KLM_API_KEY, AF_KLM_API_SECRET)

    def test___init__(self):
        assert isinstance(self.airfranceklm.api_key, str)
        assert isinstance(self.airfranceklm.api_secret, str)
        assert isinstance(self.airfranceklm.headers, dict)

        assert self.airfranceklm.headers["API-Key"] == self.AF_KLM_API_KEY
        assert self.airfranceklm.headers["Content-Type"] == "application/json"
        
    def test__make_request(self):
        with pytest.raises(HTTPError):
            self.airfranceklm._make_request(
                endpoint="/mega-invalid-endpoint-fa-sho", data=None
            )
