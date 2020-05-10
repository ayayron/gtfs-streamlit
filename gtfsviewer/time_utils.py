from datetime import date, timedelta

MIN_DATE = date(2017, 1, 1)

YESTERDAY = date.today() - timedelta(days=1)

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def is_invalid_date(selected_date: date) -> bool:
    return selected_date < MIN_DATE or selected_date > date.today() - timedelta(days=1)
