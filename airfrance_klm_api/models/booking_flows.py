from enum import Enum

from pydantic import BaseModel
from pydantic.functional_validators import field_validator

from airfrance_klm_api.utils import remove_spaces, to_upper


class BookingFlowsEnum(str, Enum):
    reward: str = "REWARD"
    corporate: str = "CORPORATE"
    leisure: str = "LEISURE"
    staff: str = "STAFF"


class BookingFlows(BaseModel):
    """
    Pydantic model that validates
    users are choosing a supported
    option.

    """

    booking_flow: BookingFlowsEnum

    @field_validator("booking_flow", mode="before")
    @classmethod
    def process_booking_flow(cls, v: str) -> str:
        return to_upper(remove_spaces(v))
