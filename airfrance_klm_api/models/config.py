from functools import cached_property
from pydantic import BaseModel
from airfrance_klm_api.models.enums import Host


class Config(BaseModel):
    API_KEY: str
    API_SECRET: str
    BASE_URL: str = "https://api.airfranceklm.com"
    CONTENT_TYPE: str = "application/x-www-form-urlencoded"
    HOST: Host = "KL"
    ADDITIONAL_HEADERS: dict = {}

    @cached_property
    def headers(self) -> dict:
        return {
            "API-Key": self.API_KEY,
            "Content-Type": self.CONTENT_TYPE,
            "AFKL-TRAVEL-Host": self.HOST,
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            **self.ADDITIONAL_HEADERS,
        }
