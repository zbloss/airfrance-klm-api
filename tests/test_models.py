import pytest
from pydantic import ValidationError

from airfrance_klm_api.models import BookingFlows, Origins, TimePeriods


class TestModels:
    def test_booking_flows(self):
        valid_inputs = ["REWARD", "CORPORATE", "LEISURE", "STAFF", "staff"]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            BookingFlows(booking_flow=valid_input)

        with pytest.raises(ValidationError):
            BookingFlows(booking_flow=invalid_input)

    def test_origins(self):
        valid_inputs = [
            "STOPOVER",
            "CITY",
            "AIRPORT",
            "BUS_STATION",
            "HELIPORT",
            "rAiLwAy_StAtIoN",
            "FERRY_station",
        ]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            Origins(origin=valid_input)

        with pytest.raises(ValidationError):
            Origins(origin=invalid_input)

    def test_time_periods(self):
        valid_inputs = [
            "day",
            "MonTh",
            "OVERALL",
        ]
        invalid_input = "SUPDUDE"

        for valid_input in valid_inputs:
            TimePeriods(time_period=valid_input)

        with pytest.raises(ValidationError):
            TimePeriods(time_period=invalid_input)
