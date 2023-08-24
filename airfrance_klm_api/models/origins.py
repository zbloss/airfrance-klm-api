from enum import Enum

from pydantic import BaseModel
from pydantic.functional_validators import field_validator

from airfrance_klm_api.utils import remove_spaces, to_upper


class OriginsEnum(str, Enum):
    stopover: str = "STOPOVER"
    city: str = "CITY"
    airport: str = "AIRPORT"
    bus_station: str = "BUS_STATION"
    heliport: str = "HELIPORT"
    railway_station: str = "RAILWAY_STATION"
    ferry_station: str = "FERRY_STATION"


class Origins(BaseModel):
    """
    Pydantic model that validates
    users are choosing a supported
    option.

    """

    origin: OriginsEnum

    @field_validator("origin", mode="before")
    @classmethod
    def process_booking_flow(cls, v: str) -> str:
        return to_upper(remove_spaces(v))