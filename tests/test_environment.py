import pytest
from pydantic import ValidationError
from airfrance_klm_api.environment import Environment


class TestEnvironment:
    TEST_API_KEY: str = "hey"
    TEST_API_SECRET: str = "there"
    TEST_LOG_LEVEL: str = "DEBUG"
    test_environment: Environment = Environment(
        API_KEY=TEST_API_KEY, API_SECRET=TEST_API_SECRET, LOG_LEVEL=TEST_LOG_LEVEL
    )

    def test___init__(self):
        assert isinstance(self.test_environment.API_KEY, str)
        assert isinstance(self.test_environment.API_SECRET, str)
        assert isinstance(self.test_environment.LOG_LEVEL, str)

    def test_invalid_api_key(self):
        with pytest.raises(ValidationError):
            Environment(API_KEY=123, API_SECRET=self.TEST_API_SECRET)

    def test_invalid_api_secret(self):
        with pytest.raises(ValidationError):
            Environment(API_KEY=self.TEST_API_KEY, API_SECRET=True)

    def test_invalid_log_level(self):
        with pytest.raises(ValidationError):
            Environment(
                API_KEY=self.TEST_API_KEY,
                API_SECRET=self.TEST_API_SECRET,
                LOG_LEVEL=123,
            )
