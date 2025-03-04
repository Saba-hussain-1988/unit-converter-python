import streamlit as st
from streamlit_analytics import track
from length_converter import length_conversion_interface
from mass_converter import mass_conversion_interface
from volume_converter import volume_conversion_interface
from temperature_converter import temperature_conversion_interface
from energy_converter import energy_conversion_interface
from currency_converter import currency_conversion_interface
from area_converter import area_conversion_interface
from frequency_converter import frequency_conversion_interface
from pressure_converter import pressure_conversion_interface
from speed_converter import speed_conversion_interface
from time_converter import time_conversion_interface

@track()
def main():
    # Color Settings
    st.sidebar.title("Color Settings")
    color = st.sidebar.selectbox("Select Color", ["Green", "Blue", "Red"])
    if color == "Green":
        primary_color = "#f0fff0"
        secondary_color = "green"
        st.markdown(
            """
            <style>
                .stApp {
                    background-color: #f0fff0;
                }
                .stApp h1 {
                    color: green !important; /* Green Title */
                }
                .sidebar .sidebar-content {
                    background-color: #799a6fc5;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif color == "Blue":
        primary_color = "#d8f5fa"
        secondary_color = "#6771fe"
        st.markdown(
            """
            <style>
                .stApp {
                    background-color: #d8f5fa;
                }
                .stApp h1 {
                    color: blue !important; /* Green Title */
                }
                .sidebar .sidebar-content {
                    background-color: #7f83b0c5;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif color == "Red":
        primary_color = "#f4dede"
        secondary_color = "#b12d2d"
        st.markdown(
            """
            <style>
                .stApp {
                    background-color: #f4dede;
                }
                .stApp h1 {
                    color: #b12d2d !important; /* Green Title */
                }
                div[data-testid="stSidebar"] {
                    background-color: #a27a7a;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    

    # Main Page
    st.title("Unit Converter by S.R.Chohan")
    st.subheader("A comprehensive unit conversion tool")
    st.write("Select a category from the sidebar to get started")

if __name__ == "__main__":
    main()

# Sidebar
st.sidebar.title("Unit Converter")
category = st.sidebar.selectbox("Select Category", ["Length", "Mass", "Volume", "Temperature", "Energy", "Currency", "Area", "Frequency", "Pressure", "Speed", "Time"])

if category == "Length":
    length_conversion_interface(primary_color, secondary_color)
elif category == "Mass":
    mass_conversion_interface(primary_color, secondary_color)
elif category == "Volume":
    volume_conversion_interface(primary_color, secondary_color)
elif category == "Temperature":
    temperature_conversion_interface(primary_color, secondary_color)
elif category == "Energy":
    energy_conversion_interface(primary_color, secondary_color)
elif category == "Currency":
    currency_conversion_interface(primary_color, secondary_color)
elif category == "Area":
    area_conversion_interface(primary_color, secondary_color)
elif category == "Frequency":
    frequency_conversion_interface(primary_color, secondary_color)
elif category == "Pressure":
    pressure_conversion_interface(primary_color, secondary_color)
elif category == "Speed":
    speed_conversion_interface(primary_color, secondary_color)
elif category == "Time":
    time_conversion_interface(primary_color, secondary_color)

