import time

import pydeck as pdk
import streamlit as st

from gtfsviewer.sidebar import generate_sidebar
from gtfsviewer.importer import GTFSFile

def run():
    st.title("GTFS Viewer")
    options = generate_sidebar(st.sidebar)

    with st.spinner("Loading GTFS data..."):
        gtfs_data = GTFSFile("data/gtfs.zip")
        gtfs_data.extractall()

    with st.spinner("Updating map..."):
        map_layers = []
        if options.display_stops:
            map_layers.append(
                pdk.Layer(
                    "ScatterplotLayer",
                    data=gtfs_data.stops,
                    get_position="[lon, lat]",
                    get_fill_color="[100, 30, 0, 160]",
                    get_radius=30,
                    pickable=True,
                )
            )
        if options.display_routes:
            map_layers.append(
                pdk.Layer(
                    "PathLayer",
                    data=gtfs_data.shapes,
                    width_scale=20,
                    width_min_pixels=1,
                    get_path="path",
                    get_width=1,
                    get_color=(0, 0, 255, 255),
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
