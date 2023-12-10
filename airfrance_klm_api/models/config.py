from functools import cached_property
from pydantic import BaseModel


class Config(BaseModel):
    API_KEY: str
    API_SECRET: str
    BASE_URL: str = "https://live.airfranceklm.com"
    ADDITIONAL_HEADERS: dict = {}

    @cached_property
    def headers(self) -> dict:
        return {
            "API-Key": self.API_KEY,
            "Content-Type": "application/json",
            **self.ADDITIONAL_HEADERS,
        }
