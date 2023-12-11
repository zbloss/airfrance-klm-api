from typing import List

from airfrance_klm_api.base import AirfranceKLM
from airfrance_klm_api.models.enums import BookingFlows, Origins, TimePeriods


class Offers(AirfranceKLM):
    endpoint_prefix: str = f"travel/offers/v3"

    def lowest_fares_by_destination(
        self,
        origin_code: str,
        destination_cities: List[str],
        from_date: str,
        until_date: str,
        origin_type: Origins = "AIRPORT",
        booking_flow: BookingFlows = "LEISURE",
        time_period: TimePeriods = "DAY",
        **kwargs,
    ):
        """
        Provides the lowest fares by destinations on the next 12 months for a given origin.

        :href: https://developer.airfranceklm.com/products/api/offers/api-reference#tag/lowest-fares-by-destination

        Args:
            origin_code : str
                String code you are leaving from.
            destination_cities : List[str]
                List of destination codes as string values.
            from_date : str
                Start of your trip in datetime format %Y-%m-%dT%H:%M:%SZ.
            until_date : str
                End of your trip in datetime format %Y-%m-%dT%H:%M:%SZ.
            origin_type : Origins
                String representing what kind of location you are leaving from.
                [Optional] default: AIRPORT.
            booking_flow : BookingFlows
                Represents a type of booking flow, i.e. the specific context in which the customer is booking a flight (eg: for leisure, as a corporate, as a staff etc.).
                [Optional] default: LEISURE.
            time_period : TimePeriods
                The different periods of time that can be considered when requesting lowest fares.
                [Optional] default: DAY.

        Returns:
            fares : list
                List of fare dictionary objects.

        Raises:
            AssertionError : If from_date passed is an invalid format.
            AssertionError : If until_date passed is an invalid format.
            AssertionError : If destination_cities is not a list.
        """

        assert len(from_date.split(":")) == len(from_date.split("-")) == 3
        assert len(from_date.split("T")) == 2

        assert len(until_date.split(":")) == len(until_date.split("-")) == 3
        assert len(until_date.split("T")) == 2

        assert isinstance(destination_cities, list)

        # origin_type = Origins(origin_type).origin
        # booking_flow = BookingFlows(booking_flow=booking_flow).booking_flow
        # time_period = TimePeriods(time_period=time_period).time_period

        payload: dict = {
            "bookingFlow": booking_flow,
            "origin": {"type": origin_type, "code": origin_code},
            "destinationCities": destination_cities,
            "type": time_period,
            "fromDate": from_date,
            "untilDate": until_date,
        }

        endpoint = f"/{self.endpoint_prefix}/lowest-fares-by-destination"
        response = self._make_request(endpoint, data=payload, post_call=True, **kwargs)

        return response


if __name__ == "__main__":
    import os
    from datetime import datetime, timedelta

    from dotenv import load_dotenv

    from airfrance_klm_api.utils import format_datetime

    load_dotenv()
    AF_KLM_API_KEY = os.getenv("AF_KLM_API_KEY")
    AF_KLM_API_SECRET = os.getenv("AF_KLM_API_SECRET")

    offers = Offers(AF_KLM_API_KEY, AF_KLM_API_SECRET, "v3")
    origin_code: str = "DTW"
    destination_cities: list = ["ORD", "ROM"]
    from_date: datetime = datetime.now()
    until_date: datetime = timedelta(days=7) + from_date

    from_date_str: str = format_datetime(from_date)
    until_date_str: str = format_datetime(until_date)

    origin_type: str = "AIRPORT"
    booking_flow: str = "LEISURE"
    time_period: str = "day"

    out = offers.lowest_fares_by_destination(
        origin_code,
        destination_cities,
        from_date_str,
        until_date_str,
        origin_type,
        booking_flow,
        time_period,
    )


# {
#     "bookingFlow": "LEISURE",
#     "origin": {
#         "type": "STOPOVER",
#         "code": "CDG"
#     },
#     "destinationCities": [
#         "AMS",
#         "PAR",
#         "LON"
#     ],
#     "type": "DAY",
#     "fromDate": "2019-08-24T14:15:22Z",
#     "untilDate": "2019-08-24T14:15:22Z"
# }
