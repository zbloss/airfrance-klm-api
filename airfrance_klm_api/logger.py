import logging
from airfrance_klm_api.models.enums import LogLevelEnum
from pydantic import BaseModel
from functools import cached_property


class Logger(BaseModel):
    module: str
    log_level: LogLevelEnum = "INFO"
    logging_format: str = "%(asctime)s - %(levelname)s - %(name)s: %(message)s"

    @cached_property
    def _log_level(self):
        level = logging.INFO
        if self.log_level == "DEBUG":
            level = logging.DEBUG
        elif self.log_level == "INFO":
            level = logging.INFO
        elif self.log_level == "WARNING":
            level = logging.WARNING
        elif self.log_level == "ERROR":
            level = logging.ERROR
        elif self.log_level == "CRITICAL":
            level = logging.CRITICAL
        else:
            raise ValueError(f"Invalid log level: {self.log_level}")

        return level

    def get_logger(self):
        logging.basicConfig(level=self._log_level, format=self.logging_format)
        return logging.getLogger(self.module)
