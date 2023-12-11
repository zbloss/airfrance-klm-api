import pytest
from datetime import datetime
from pydantic import ValidationError
from airfrance_klm_api.models.datetime import DateTime


class TestDateTime:
    valid_datetime_format: str = "%Y-%m-%dT%H:%M:%SZ"
    valid_datetime: datetime = datetime.now().strftime(valid_datetime_format)

    def test_datetime_valid(self):
        dt = DateTime(datetime=self.valid_datetime)
        dt = DateTime(datetime=self.valid_datetime)
        assert dt.datetime == self.valid_datetime

    def test_datetime_invalid(self):
        with pytest.raises(ValidationError):
            DateTime(datetime="invalid_datetime")
