from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from airfrance_klm_api.offers import Offers
from airfrance_klm_api.utils import format_datetime
from airfrance_klm_api.models.config import Config
from requests.exceptions import ConnectionError


load_dotenv()


class TestOffers:
    api_key: str = "hey"
    api_secret: str = "there"
    base_url: str = "https://live.airfranceklm.com"
    default_config: Config = Config(API_KEY=api_key, API_SECRET=api_secret)
    offers = Offers(config=default_config)

    def test___init__(self):
        assert isinstance(self.offers.config.API_KEY, str)
        assert isinstance(self.offers.config.API_SECRET, str)
        assert isinstance(self.offers.config.headers, dict)

        assert self.offers.config.headers["API-Key"] == self.api_key
        assert self.offers.config.headers["Content-Type"] == "application/json"

    @pytest.mark.integration_test
    def test_lowest_fares_by_destination_invalid(self):
        origin_code: str = "DTW"
        destination_cities: list = ["ORD", "ROM"]
        from_date: datetime = datetime.now()
        until_date: datetime = timedelta(days=7) + from_date

        from_date_str: str = format_datetime(from_date)
        until_date_str: str = format_datetime(until_date)

        origin_type: str = "AIRPORT"
        booking_flow: str = "LEISURE"
        time_period: str = "DAY"

        with pytest.raises(ConnectionError):
            self.offers.lowest_fares_by_destination(
                origin_code,
                destination_cities,
                from_date_str,
                until_date_str,
                origin_type,
                booking_flow,
                time_period,
                max_retries=1,
                backoff_factor=1,
            )
