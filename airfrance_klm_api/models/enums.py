from enum import StrEnum


class TimePeriods(StrEnum):
    day: str = "DAY"
    month: str = "MONTH"
    overall: str = "OVERALL"


class Origins(StrEnum):
    stopover: str = "STOPOVER"
    city: str = "CITY"
    airport: str = "AIRPORT"
    bus_station: str = "BUS_STATION"
    heliport: str = "HELIPORT"
    railway_station: str = "RAILWAY_STATION"
    ferry_station: str = "FERRY_STATION"


class BookingFlows(StrEnum):
    reward: str = "REWARD"
    corporate: str = "CORPORATE"
    leisure: str = "LEISURE"
    staff: str = "STAFF"


class LogLevel(StrEnum):
    debug: str = "DEBUG"
    info: str = "INFO"
    warning: str = "WARNING"
    error: str = "ERROR"
    critical: str = "CRITICAL"

class Host(StrEnum):
    airfrance: str = "AF"
    klm: str = "KL"