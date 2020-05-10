from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass(frozen=True)
class Agency:
    id: str
    name: str
    url: str
    tz: str
    lang: str


@dataclass(frozen=True)
class Calendar:
    service_id: int
    monday: bool
    tuesday: bool
    wednesday: bool
    tursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    start_date: str
    end_date: str


@dataclass(frozen=True)
class CalendarDates:
    service_id: int
    date: str
    exception_type: int


@dataclass(frozen=True)
class FareAttributes:
    id: int
    price: float
    currency: str
    payment_method: str
    transfers: Optional[int]
    transfer_duration: Optional[int]  # time in seconds


@dataclass(frozen=True)
class FareRules:
    fare_id: int
    route_id: int
    origin_id: int
    destination_id: int
    contains_id: int


class RouteType(Enum):
    express = "EXPRESS"
    rapid = "RAPID"


@dataclass(frozen=True)
class Routes:
    id: int
    agency_id: str
    short_name: str
    long_name: str
    description: str
    type: RouteType
    url: str
    color: str
    text_color: str


@dataclass(frozen=True)
class Shapes:
    id: int
    lon: float
    lat: float
    seq: int
    distance_from_start: int


@dataclass(frozen=True)
class StopTimes:
    trip_id: int
    arrival_time: str
    departure_time: str
    stop_id: str
    stop_sequence: str
    stop_headsign: str
    pickup_type: str
    drop_off_type: str
    shape_dist_traveled: Optional[int]


@dataclass(frozen=True)
class Stops:
    id: int
    name: str
    description: str
    lat: float
    lon: float
    zone_id: int
    url: str


@dataclass(frozen=True)
class Trips:
    route_id: int
    service_id: int
    trip_id: int
    trip_headsign: str
    direction_id: int
    block_id: int
    shape_id: int
