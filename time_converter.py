import streamlit as st

def time_converter(value, from_unit, to_unit):
    if from_unit == "Second" and to_unit == "Minute":
        return value / 60
    elif from_unit == "Second" and to_unit == "Hour":
        return value / 3600
    elif from_unit == "Second" and to_unit == "Day":
        return value / 86400
    elif from_unit == "Minute" and to_unit == "Second":
        return value * 60
    elif from_unit == "Minute" and to_unit == "Hour":
        return value / 60
    elif from_unit == "Minute" and to_unit == "Day":
        return value / 1440
    elif from_unit == "Hour" and to_unit == "Second":
        return value * 3600
    elif from_unit == "Hour" and to_unit == "Minute":
        return value * 60
    elif from_unit == "Hour" and to_unit == "Day":
        return value / 24
    elif from_unit == "Day" and to_unit == "Second":
        return value * 86400
    elif from_unit == "Day" and to_unit == "Minute":
        return value * 1440
    elif from_unit == "Day" and to_unit == "Hour":
        return value * 24
    else:
        return "Invalid units"


def time_conversion_interface():
    st.title("Time Converter")
    st.subheader("Convert between different units of time")
    
    value = st.number_input("Enter time value")
    from_unit = st.selectbox("Select from unit", ["Second", "Minute", "Hour", "Day"])
    to_unit = st.selectbox("Select to unit", ["Second", "Minute", "Hour", "Day"])
    
    if st.button("Convert"):
        result = time_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")


