import time

import pydeck as pdk
import streamlit as st

from gtfsviewer.sidebar import generate_sidebar
from gtfsviewer.importer import get_stops


def run():
    st.title("GTFS Viewer")
    options = generate_sidebar(st.sidebar)

    with st.spinner("Loading data..."):
        map_layers = []
        time.sleep(1)
        if options.display_stops:
            stops = get_stops()
            map_layers.append(
                pdk.Layer(
                    "ScatterplotLayer",
                    data=stops,
                    get_position="[lon, lat]",
                    get_fill_color="[100, 30, 0, 160]",
                    get_radius=30,
                )
            )

        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=pdk.ViewState(
                    latitude=37.76, longitude=-122.4, zoom=11, bearing=0, pitch=0
                ),
                layers=[map_layers],
            )
        )


if __name__ == "__main__":
    run()
