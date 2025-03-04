import streamlit as st

def frequency_converter(value, from_unit, to_unit):
    if from_unit == "Hertz" and to_unit == "Kilohertz":
        return value / 1000
    elif from_unit == "Hertz" and to_unit == "Megahertz":
        return value / 1000000
    elif from_unit == "Hertz" and to_unit == "Gigahertz":
        return value / 1000000000
    elif from_unit == "Kilohertz" and to_unit == "Hertz":
        return value * 1000
    elif from_unit == "Kilohertz" and to_unit == "Megahertz":
        return value / 1000
    elif from_unit == "Kilohertz" and to_unit == "Gigahertz":
        return value / 1000000
    elif from_unit == "Megahertz" and to_unit == "Hertz":
        return value * 1000000
    elif from_unit == "Megahertz" and to_unit == "Kilohertz":
        return value * 1000
    elif from_unit == "Megahertz" and to_unit == "Gigahertz":
        return value / 1000
    elif from_unit == "Gigahertz" and to_unit == "Hertz":
        return value * 1000000000
    elif from_unit == "Gigahertz" and to_unit == "Kilohertz":
        return value * 1000000
    elif from_unit == "Gigahertz" and to_unit == "Megahertz":
        return value * 1000
    else:
        return "Invalid units"

def frequency_conversion_interface():
    st.title("Frequency Converter")
    st.subheader("Convert between different units of frequency")
    
    value = st.number_input("Enter frequency value")
    from_unit = st.selectbox("Select from unit", ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"])
    to_unit = st.selectbox("Select to unit", ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"])
    
    if st.button("Convert"):
        result = frequency_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")
