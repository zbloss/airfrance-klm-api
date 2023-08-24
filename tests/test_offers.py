import os
from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from airfrance_klm_api.offers import Offers
from airfrance_klm_api.utils import format_datetime

load_dotenv()


class TestOffers:
    AF_KLM_API_KEY = os.getenv("AF_KLM_API_KEY")
    AF_KLM_API_SECRET = os.getenv("AF_KLM_API_SECRET")

    offers = Offers(AF_KLM_API_KEY, AF_KLM_API_SECRET)

    def test___init__(self):
        assert isinstance(self.offers.api_key, str)
        assert isinstance(self.offers.api_secret, str)
        assert isinstance(self.offers.headers, dict)

        assert self.offers.headers["API-Key"] == self.AF_KLM_API_KEY
        assert self.offers.headers["Content-Type"] == "application/json"

    def test_lowest_fares_by_destination(self):
        origin_code: str = "DTW"
        destination_cities: list = ["ORD", "ROM"]
        from_date: datetime = datetime.now()
        until_date: datetime = timedelta(days=7) + from_date

        from_date_str: str = format_datetime(from_date)
        until_date_str: str = format_datetime(until_date)

        origin_type: str = "AIRPORT"
        booking_flow: str = "LEISURE"
        time_period: str = "day"

        out = self.offers.lowest_fares_by_destination(
            origin_code,
            destination_cities,
            from_date_str,
            until_date_str,
            origin_type,
            booking_flow,
            time_period,
        )

        assert isinstance(out, dict)
