from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from airfrance_klm_api.models.enums import OriginsEnum
from airfrance_klm_api.utils import remove_spaces, to_upper


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
