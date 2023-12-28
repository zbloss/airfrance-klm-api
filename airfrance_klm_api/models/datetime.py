from pydantic import BaseModel, Field
from datetime import datetime


class DateTime(BaseModel):
    datetime: datetime

    def to_string(self):
        return self.datetime.strftime("%Y-%m-%dT%H:%M:%S")
