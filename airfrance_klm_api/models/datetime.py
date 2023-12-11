from pydantic import BaseModel, Field


class DateTime(BaseModel):
    datetime: str = Field(
        str,
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?([Zz]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?",
    )
