import pytest
from requests.exceptions import ConnectionError
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
    def test__make_request_invalid(self):
        with pytest.raises(ConnectionError):
            self.airfranceklm._make_request(
                endpoint="/mega-invalid-endpoint-fa-sho",
                post_call=False,
                data=None,
                max_retries=1,
                backoff_factor=1,
            )

    @pytest.mark.integration_test
    def test__make_request_valid(self):
        config: Config = Config(
            API_KEY=self.api_key,
            API_SECRET=self.api_secret,
            BASE_URL="https://google.com",
        )
        airfranceklm = AirfranceKLM(config=config)

        out = airfranceklm._make_request(
            endpoint="/",
            post_call=False,
            data=None,
            max_retries=1,
            backoff_factor=1,
        )
        assert isinstance(out, dict)
