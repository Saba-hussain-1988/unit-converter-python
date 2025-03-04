import streamlit as st

def speed_converter(value, from_unit, to_unit):
    if from_unit == "Meter per second" and to_unit == "Kilometer per hour":
        return value * 3.6
    elif from_unit == "Meter per second" and to_unit == "Mile per hour":
        return value * 2.23694
    elif from_unit == "Kilometer per hour" and to_unit == "Meter per second":
        return value / 3.6
    elif from_unit == "Kilometer per hour" and to_unit == "Mile per hour":
        return value * 0.621371
    elif from_unit == "Mile per hour" and to_unit == "Meter per second":
        return value / 2.23694
    elif from_unit == "Mile per hour" and to_unit == "Kilometer per hour":
        return value * 1.60934
    else:
        return "Invalid units"

def speed_conversion_interface():
    st.title("Speed Converter")
    st.subheader("Convert between different units of speed")
    
    value = st.number_input("Enter speed value")
    from_unit = st.selectbox("Select from unit", ["Meter per second", "Kilometer per hour", "Mile per hour"])
    to_unit = st.selectbox("Select to unit", ["Meter per second", "Kilometer per hour", "Mile per hour"])
    
    if st.button("Convert"):
        result = speed_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")
