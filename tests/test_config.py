from airfrance_klm_api.models.config import Config
from pydantic import ValidationError
import pytest


class TestConfig:
    api_key: str = "hey"
    api_secret: str = "there"
    base_url: str = "https://live.airfranceklm.com"
    default_config: Config = Config(API_KEY=api_key, API_SECRET=api_secret)

    def test___init__(self):
        assert isinstance(self.default_config.API_KEY, str)
        assert isinstance(self.default_config.API_SECRET, str)
        assert isinstance(self.default_config.BASE_URL, str)
        assert isinstance(self.default_config.ADDITIONAL_HEADERS, dict)

    def test_headers(self):
        assert isinstance(self.default_config.headers, dict)
        assert self.default_config.headers["API-Key"] == self.api_key
        assert self.default_config.headers["Content-Type"] == "application/json"
        assert len(self.default_config.headers.keys()) == 2

    def test_invalid_api_key(self):
        with pytest.raises(ValidationError):
            Config(API_KEY=123, API_SECRET=self.api_secret)

    def test_additional_headers(self):
        additional_headers: dict = {"X-Test": "test"}

        config: Config = Config(
            API_KEY=self.api_key,
            API_SECRET=self.api_secret,
            ADDITIONAL_HEADERS=additional_headers,
        )

        assert isinstance(config.headers, dict)
        assert config.headers["API-Key"] == self.api_key
        assert config.headers["Content-Type"] == "application/json"
        assert config.headers["X-Test"] == "test"
        assert len(config.headers.keys()) == 3

    def test_invalid_additional_headers(self):
        with pytest.raises(ValidationError):
            Config(
                API_KEY=self.api_key, API_SECRET=self.api_secret, ADDITIONAL_HEADERS=123
            )
