import streamlit as st


st.title("Unit Converter by S.R.Cohan")
st.header("About the App")
st.write("A comprehensive unit conversion tool designed to simplify your calculations. Convert units across various categories, including:")
unordered_list = [
    "Length (e.g., meters to feet, kilometers to miles)"
    "Mass (e.g., grams to pounds, kilograms to ounces)"
    "Volume (e.g., liters to gallons, milliliters to cups)"
    "Temperature (e.g., Celsius to Fahrenheit, Kelvin to Celsius)"
    "Energy (e.g., joules to calories, kilowatt-hours to British Thermal Units)"
    "Currency (e.g., USD to EUR, INR to USD)"
    "Area (e.g., square meters to square feet, acres to hectares)"
    "Frequency (e.g., hertz to kilohertz, megahertz to gigahertz)"
    "Pressure (e.g., pascals to pounds per square inch, atmospheres to bar)"
    "Speed (e.g., meters per second to miles per hour, kilometers per hour to knots)"
    "Time (e.g., seconds to minutes, hours to days)"
]
for item in unordered_list:
    print(f"* {item}")

st.write("With this intuitive unit converter, you can easily switch between different units of measurement, saving you time and effort in your calculations.")
