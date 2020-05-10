from dataclasses import dataclass
from datetime import date
import requests
from typing import List
from zipfile import ZipFile
import os


import streamlit as st
import pandas as pd

import gtfsviewer.gtfs as gtfs

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

TMP_FILE_DIR = "data/"


class GTFSFile:
    def __init__(self, filename: str):
        self.filename = filename

        self._agency = None
        self._calendar = None
        self._calendar_dates = None
        self._fare_attributes = None
        self._fare_rules = None
        self._routes = None
        self._shapes = None
        self._stop_times = None
        self._stops = None
        self._trips = None

    @st.cache
    def extractall(self):
        with ZipFile(self.filename, "r") as zip_obj:
            zip_obj.extractall(TMP_FILE_DIR)

    def _read_file_from_zip(self, filetype, columns: List = None) -> pd.DataFrame:
        df = pd.read_csv(os.path.join(TMP_FILE_DIR, f"{filetype}.txt"))
        if columns:
            df.columns = columns
        return df

    @property
    def agency(self):
        if self._agency is None:
            self._agency = self._read_file_from_zip("agency")
        return self._agency

    @property
    def routes(self):
        if self._routes is None:
            self._routes = self._read_file_from_zip("routes")
        return self._routes

    @property
    def shapes(self):
        if self._shapes is None:
            shapes = self._read_file_from_zip("shapes")
            shapes["lng_lat"] = shapes.apply(
                lambda x: [x["shape_pt_lon"], x["shape_pt_lat"]], axis=1
            )
            self._shapes = (
                shapes.groupby("shape_id")["lng_lat"].apply(list).reset_index()
            )

        self._shapes.columns = ["s_id", "path"]
        return self._shapes

    @property
    def stops(self):
        if self._stops is None:
            columns = [
                "id",
                "code",
                "name",
                "description",
                "lat",
                "lon",
                "zone_id",
                "url",
            ]
            self._stops = self._read_file_from_zip("stops", columns)
        return self._stops


def download_data(requested_date: date = None):
    date_str = LATEST if not requested_date else requested_date

    ### filename -> newfilename wit date
    return requests.get(TRANSIT_FEED_URL.format(date_str))
