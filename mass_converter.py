import streamlit as st

def mass_converter(value, from_unit, to_unit):
    if from_unit == "Gram" and to_unit == "Kilogram":
        return value / 1000
    elif from_unit == "Gram" and to_unit == "Milligram":
        return value * 1000
    elif from_unit == "Gram" and to_unit == "Ton":
        return value / 1000000
    elif from_unit == "Kilogram" and to_unit == "Gram":
        return value * 1000
    elif from_unit == "Kilogram" and to_unit == "Milligram":
        return value * 1000000
    elif from_unit == "Kilogram" and to_unit == "Ton":
        return value / 1000
    elif from_unit == "Milligram" and to_unit == "Gram":
        return value / 1000
    elif from_unit == "Milligram" and to_unit == "Kilogram":
        return value / 1000000
    elif from_unit == "Milligram" and to_unit == "Ton":
        return value / 1000000000
    elif from_unit == "Ton" and to_unit == "Gram":
        return value * 1000000
    elif from_unit == "Ton" and to_unit == "Kilogram":
        return value * 1000
    elif from_unit == "Ton" and to_unit == "Milligram":
        return value * 1000000000

    else:
        return "Invalid units"

def mass_conversion_interface(primary_color, secondary_color):
    st.title("Mass Converter")
    st.subheader("Convert between different units of mass")
    
    value = st.number_input("Enter mass value")
    from_unit = st.selectbox("Select from unit", ["Gram", "Kilogram", "Milligram", "Ton"])
    to_unit = st.selectbox("Select to unit", ["Gram", "Kilogram", "Milligram", "Ton"])
    
    if st.button("Convert"):
        result = mass_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")
