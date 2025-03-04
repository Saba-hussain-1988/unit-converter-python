import streamlit as st

def length_converter(value, from_unit, to_unit):
    if from_unit == "Meter" and to_unit == "Centimeter":
        return value * 100
    elif from_unit == "Meter" and to_unit == "Millimeter":
        return value * 1000
    elif from_unit == "Meter" and to_unit == "Kilometer":
        return value / 1000
    elif from_unit == "Meter" and to_unit == "Mile":
        return value / 1609.34
    elif from_unit == "Centimeter" and to_unit == "Meter":
        return value / 100
    elif from_unit == "Centimeter" and to_unit == "Millimeter":
        return value * 10
    elif from_unit == "Centimeter" and to_unit == "Kilometer":
        return value / 100000
    elif from_unit == "Centimeter" and to_unit == "Mile":
        return value / 160934
    elif from_unit == "Millimeter" and to_unit == "Meter":
        return value / 1000
    elif from_unit == "Millimeter" and to_unit == "Centimeter":
        return value / 10
    elif from_unit == "Millimeter" and to_unit == "Kilometer":
        return value / 1000000
    elif from_unit == "Millimeter" and to_unit == "Mile":
        return value / 1609340
    elif from_unit == "Kilometer" and to_unit == "Meter":
        return value * 1000
    elif from_unit == "Kilometer" and to_unit == "Centimeter":
        return value * 100000
    elif from_unit == "Kilometer" and to_unit == "Millimeter":
        return value * 1000000
    elif from_unit == "Kilometer" and to_unit == "Mile":
        return value / 1.60934
    elif from_unit == "Mile" and to_unit == "Meter":
        return value * 1609.34
    elif from_unit == "Mile" and to_unit == "Centimeter":
        return value * 160934
    elif from_unit == "Mile" and to_unit == "Millimeter":
        return value * 1609340
    elif from_unit == "Mile" and to_unit == "Kilometer":
        return value * 1.60934
    else:
        return "Invalid units"

def length_conversion_interface():
    st.title("Length Converter")
    st.subheader("Convert between different units of length")
    
    value = st.number_input("Enter length value")
    from_unit = st.selectbox("Select from unit", ["Meter", "Centimeter", "Millimeter", "Kilometer", "Mile"])
    to_unit = st.selectbox("Select to unit", ["Meter", "Centimeter", "Millimeter", "Kilometer", "Mile"])
    
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")


