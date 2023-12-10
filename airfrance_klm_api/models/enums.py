from enum import StrEnum


class TimePeriodsEnum(StrEnum):
    day: str = "DAY"
    month: str = "MONTH"
    overall: str = "OVERALL"


class OriginsEnum(StrEnum):
    stopover: str = "STOPOVER"
    city: str = "CITY"
    airport: str = "AIRPORT"
    bus_station: str = "BUS_STATION"
    heliport: str = "HELIPORT"
    railway_station: str = "RAILWAY_STATION"
    ferry_station: str = "FERRY_STATION"


class BookingFlowsEnum(StrEnum):
    reward: str = "REWARD"
    corporate: str = "CORPORATE"
    leisure: str = "LEISURE"
    staff: str = "STAFF"


class LogLevelEnum(StrEnum):
    debug: str = "DEBUG"
    info: str = "INFO"
    warning: str = "WARNING"
    error: str = "ERROR"
    critical: str = "CRITICAL"
