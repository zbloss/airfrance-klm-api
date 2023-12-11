import os
from pydantic import BaseModel
from dotenv import load_dotenv
from airfrance_klm_api.models.enums import LogLevel
from airfrance_klm_api.logger import Logger

load_dotenv()

API_KEY: str = os.getenv("AF_KLM_API_KEY")
API_SECRET: str = os.getenv("AF_KLM_API_SECRET")
LOG_LEVEL: LogLevel = os.getenv("LOG_LEVEL", "INFO")
logger = Logger(module=__name__, log_level=LOG_LEVEL).get_logger()


class Environment(BaseModel):
    API_KEY: str = API_KEY
    API_SECRET: str = API_SECRET
    LOG_LEVEL: LogLevel = LOG_LEVEL


for key, value in Environment().model_dump().items():
    logger.debug(f"{key}: {value}")
