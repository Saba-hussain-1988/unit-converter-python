
import streamlit as st

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid units"
def temperature_conversion_interface():
    st.title("Temperature Converter")
    st.subheader("Convert between different units of temperature")
    
    value = st.number_input("Enter temperature value")
    from_unit = st.selectbox("Select from unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("Select to unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")


