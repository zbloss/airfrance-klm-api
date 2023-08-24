from enum import Enum

from pydantic import BaseModel
from pydantic.functional_validators import field_validator

from airfrance_klm_api.utils import remove_spaces, to_upper


class TimePeriodsEnum(str, Enum):
    day: str = "DAY"
    month: str = "MONTH"
    overall: str = "OVERALL"


class TimePeriods(BaseModel):
    """
    Pydantic model that validates
    users are choosing a supported
    option.

    """

    time_period: TimePeriodsEnum

    @field_validator("time_period", mode="before")
    @classmethod
    def process_booking_flow(cls, v: str) -> str:
        return to_upper(remove_spaces(v))
