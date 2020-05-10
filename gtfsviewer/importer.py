from datetime import date
import requests

import streamlit as st
import pandas as pd

from . import gtfs

TRANSIT_FEED_URL = "https://transitfeeds.com/p/sfmta/60/{}/download"

LATEST = "latest"

DATE_FORMAT = r"%YYYY%dd%dd"


FILENAME = "gtfs.zip"

FILES_IN_ZIP = {
    "agency": gtfs.Agency,
    "calendar": gtfs.Calendar,
    "calendar_dates": gtfs.CalendarDates,
    "fare_attributes": gtfs.FareAttributes,
    "fare_rules": gtfs.FareRules,
    "routes": gtfs.Routes,
    "shapes": gtfs.Shapes,
    "stop_times": gtfs.StopTimes,
    "stops": gtfs.Stops,
    "trips": gtfs.Trips,
}


def download_data(requested_date: date = None):
    date_str = LATEST if not requested_date else requested_date

    ### filename -> newfilename wit date
    return requests.get(TRANSIT_FEED_URL.format(date_str))


def extract_data(zip_file: str):
    with open(zip_file, "r") as f:
        for filename, data_type in FILES_IN_ZIP:
            # parse data
            continue


@st.cache
def get_route_shapes() -> pd.DataFrame:
    shapes = pd.read_csv("sample_data/shapes.txt")
    return shapes


@st.cache
def get_stops() -> pd.DataFrame:
    stops = pd.read_csv("sample_data/stops.txt")
    stops.columns = [
        "id",
        "code",
        "name",
        "description",
        "lat",
        "lon",
        "zone_id",
        "url",
    ]
    return stops
