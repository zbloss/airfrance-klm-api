import pytest
from pydantic import ValidationError

from airfrance_klm_api.models.enums import BookingFlows, Origins, TimePeriods


class TestModels:
    def test_booking_flows(self):
        valid_inputs = ["REWARD", "CORPORATE", "LEISURE", "STAFF"]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            BookingFlows(valid_input)

        with pytest.raises(ValueError):
            BookingFlows(invalid_input)

    def test_origins(self):
        valid_inputs = [
            "STOPOVER",
            "CITY",
            "AIRPORT",
            "BUS_STATION",
            "HELIPORT",
            "RAILWAY_STATION",
            "FERRY_STATION",
        ]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            Origins(valid_input)

        with pytest.raises(ValueError):
            Origins(invalid_input)

    def test_time_periods(self):
        valid_inputs = [
            "DAY",
            "MONTH",
            "OVERALL",
        ]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            TimePeriods(valid_input)

        with pytest.raises(ValueError):
            TimePeriods(invalid_input)
