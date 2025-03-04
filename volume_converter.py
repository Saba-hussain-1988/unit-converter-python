import streamlit as st

def milliliter_to_liter(value):
    return value / 1000

def liter_to_milliliter(value):
    return value * 1000

def liter_to_gallon(value):
    return value / 3.785

def gallon_to_liter(value):
    return value * 3.785

def volume_converter(value, from_unit, to_unit):
    if from_unit == "Milliliter" and to_unit == "Liter":
        return milliliter_to_liter(value)
    elif from_unit == "Liter" and to_unit == "Milliliter":
        return liter_to_milliliter(value)
    elif from_unit == "Liter" and to_unit == "Gallon":
        return liter_to_gallon(value)
    elif from_unit == "Gallon" and to_unit == "Liter":
        return gallon_to_liter(value)
    else:
        return "Invalid units"

def volume_conversion_interface(primary_color, secondary_color):
    st.title("Volume Converter")
    st.subheader("Convert between different units of volume")
    
    value = st.number_input("Enter volume value")
    from_unit = st.selectbox("Select from unit", ["Milliliter", "Liter", "Gallon"])
    to_unit = st.selectbox("Select to unit", ["Milliliter", "Liter", "Gallon"])
    
    if st.button("Convert"):
        result = volume_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

