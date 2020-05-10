from dataclasses import dataclass
from datetime import date

import streamlit as st

from .time_utils import is_invalid_date, MIN_DATE, WEEKDAYS, YESTERDAY


FILTERS = ["Date", "Hour", "Weekday"]


@dataclass(frozen=True)
class SelectedOptions:
    display_stops: bool


def generate_sidebar(sb: st.sidebar):
    filter_type = select_filter_type(sb)
    if filter_type == "Date":
        selected_date = select_date(sb)
        st.write(selected_date)
    elif filter_type == "Hour":
        selected_hour = select_hour(sb)
        st.write(selected_hour)
    elif filter_type == "Weekday":
        selected_weekday = select_weekday(sb)
        st.write(selected_weekday)
    else:
        st.error(f"Error: Filter type {filter_type} is invalid.")

    display_stops = sb.checkbox("Show Stops")
    display_routes = sb.checkbox("Show Routes")
    return SelectedOptions(display_stops)


def select_filter_type(sb):
    return sb.selectbox("Select Filter Type", FILTERS)


def select_date(sb) -> date:
    selected_date = sb.date_input("Date", YESTERDAY)
    if is_invalid_date(selected_date):
        st.error(f"Error: Start date must be on or after {MIN_DATE} and before today")
    return selected_date


def select_hour(sb: st.sidebar) -> int:
    return sb.slider("Hour", 0, 23, 9)


def select_weekday(sb: st.sidebar) -> str:
    return sb.selectbox("Weekday", WEEKDAYS)
