from typing import List

import time
from airfrance_klm_api.base import AirfranceKLM
from airfrance_klm_api.models.enums import BookingFlows, Origins, TimePeriods
from airfrance_klm_api.models.datetime import DateTime


class Offers(AirfranceKLM):
    def reference_data_deals(
        self, endpoint: str = "opendata/offers/v3/reference-data/deals", **kwargs
    ) -> dict:
        """
        Provides a list of `best deals` as advertised by Air France and KLM.

        Args:
            endpoint : str
                Endpoint to call. [Optional]
                                  default: reference-data/deals.

        Returns:
            deals : dict
                Dictionary of deals organized by origin.

        :href: https://developer.airfranceklm.com/products/api/offers/api-reference#tag/reference-data-deals
        """

        endpoint = f"/{endpoint}"
        deals = self._make_request(endpoint, post_call=False, **kwargs)
        return deals

    def lowest_fares_by_destination(
        self,
        origin_code: str,
        destination_cities: List[str],
        from_date: DateTime,
        until_date: DateTime,
        origin_type: Origins = "AIRPORT",
        booking_flow: BookingFlows = "LEISURE",
        time_period: TimePeriods = "DAY",
        **kwargs,
    ) -> dict:
        """
        Provides the lowest fares by destinations on the next 12 months for a given origin.

        :href: https://developer.airfranceklm.com/products/api/offers/api-reference#tag/lowest-fares-by-destination

        Args:
            origin_code : str
                String code you are leaving from.
            destination_cities : List[str]
                List of destination codes as string values.
            from_date : DateTime
                Start of your trip in datetime format %Y-%m-%dT%H:%M:%SZ.
            until_date : DateTime
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
            fares : dict
                Fare dictionary objects with the keys `origin`, `destinationCities` 
                and `disclaimer`. Fares are stored under the `destinationCities` key.

        Raises:
            pydantic.ValidationError : If from_date passed is an invalid format.
            pydantic.ValidationError : If until_date passed is an invalid format.
            AssertionError : If destination_cities is not a list.
        """

        assert isinstance(destination_cities, list)

        payload: dict = {
            "bookingFlow": booking_flow,
            "origin": {"type": origin_type, "code": origin_code},
            "destinationCities": destination_cities,
            "type": time_period,
            "fromDate": from_date,
            "untilDate": until_date,
        }

        endpoint = f"/opendata/offers/v3/lowest-fares-by-destination"
        fares = self._make_request(endpoint, data=payload, post_call=True, **kwargs)
        return fares
