import streamlit as st

def area_converter(value, from_unit, to_unit):
    if from_unit == "Square Meter" and to_unit == "Square Kilometer":
        return value / 1000000
    elif from_unit == "Square Meter" and to_unit == "Square Mile":
        return value / 2589988.11
    elif from_unit == "Square Meter" and to_unit == "Acre":
        return value / 4046.856422
    elif from_unit == "Square Meter" and to_unit == "Hectare":
        return value / 10000
    elif from_unit == "Square Kilometer" and to_unit == "Square Meter":
        return value * 1000000
    elif from_unit == "Square Kilometer" and to_unit == "Square Mile":
        return value * 0.386102
    elif from_unit == "Square Kilometer" and to_unit == "Acre":
        return value * 247.105
    elif from_unit == "Square Kilometer" and to_unit == "Hectare":
        return value * 100
    elif from_unit == "Square Mile" and to_unit == "Square Meter":
        return value * 2589988.11
    elif from_unit == "Square Mile" and to_unit == "Square Kilometer":
        return value / 0.386102
    elif from_unit == "Square Mile" and to_unit == "Acre":
        return value * 640
    elif from_unit == "Square Mile" and to_unit == "Hectare":
        return value * 259
    elif from_unit == "Acre" and to_unit == "Square Meter":
        return value * 4046.856422
    elif from_unit == "Acre" and to_unit == "Square Kilometer":
        return value / 247.105
    elif from_unit == "Acre" and to_unit == "Square Mile":
        return value / 640
    elif from_unit == "Acre" and to_unit == "Hectare":
        return value / 2.47105
    elif from_unit == "Hectare" and to_unit == "Square Meter":
        return value * 10000
    elif from_unit == "Hectare" and to_unit == "Square Kilometer":
        return value / 100
    elif from_unit == "Hectare" and to_unit == "Square Mile":
        return value / 259
    elif from_unit == "Hectare" and to_unit == "Acre":
        return value * 2.47105
    else:
        return "Invalid units"

def area_conversion_interface(primary_color, secondary_color):
    st.title("Area Converter")
    st.subheader("Convert between different units of area")
    
    value = st.number_input("Enter area value")
    from_unit = st.selectbox("Select from unit", ["Square Meter", "Square Kilometer", "Square Mile", "Acre", "Hectare"])
    to_unit = st.selectbox("Select to unit", ["Square Meter", "Square Kilometer", "Square Mile", "Acre", "Hectare"])
    
    if st.button("Convert"):
        result = area_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")
