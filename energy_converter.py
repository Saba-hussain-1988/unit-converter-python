import streamlit as st

def energy_converter(value, from_unit, to_unit):
    if from_unit == "Joule" and to_unit == "Kilojoule":
        return value / 1000
    elif from_unit == "Joule" and to_unit == "Megajoule":
        return value / 1000000
    elif from_unit == "Joule" and to_unit == "Gigajoule":
        return value / 1000000000
    elif from_unit == "Joule" and to_unit == "Calorie":
        return value / 4.184
    elif from_unit == "Kilojoule" and to_unit == "Joule":
        return value * 1000
    elif from_unit == "Kilojoule" and to_unit == "Megajoule":
        return value / 1000
    elif from_unit == "Kilojoule" and to_unit == "Gigajoule":
        return value / 1000000
    elif from_unit == "Kilojoule" and to_unit == "Calorie":
        return value / 4.184 * 1000
    elif from_unit == "Megajoule" and to_unit == "Joule":
        return value * 1000000
    elif from_unit == "Megajoule" and to_unit == "Kilojoule":
        return value * 1000
    elif from_unit == "Megajoule" and to_unit == "Gigajoule":
        return value / 1000
    elif from_unit == "Megajoule" and to_unit == "Calorie":
        return value / 4.184 * 1000000
    elif from_unit == "Gigajoule" and to_unit == "Joule":
        return value * 1000000000
    elif from_unit == "Gigajoule" and to_unit == "Kilojoule":
        return value * 1000000
    elif from_unit == "Gigajoule" and to_unit == "Megajoule":
        return value * 1000
    elif from_unit == "Gigajoule" and to_unit == "Calorie":
        return value / 4.184 * 1000000000
    elif from_unit == "Calorie" and to_unit == "Joule":
        return value * 4.184
    elif from_unit == "Calorie" and to_unit == "Kilojoule":
        return value / 1000 * 4.184
    elif from_unit == "Calorie" and to_unit == "Megajoule":
        return value / 1000000 * 4.184
    elif from_unit == "Calorie" and to_unit == "Gigajoule":
        return value / 1000000000 * 4.184
    else:
        return "Invalid units"

def energy_conversion_interface(primary_color, secondary_color):
    st.title("Energy Converter")
    st.subheader("Convert between different units of energy")
    
    value = st.number_input("Enter energy value")
    from_unit = st.selectbox("Select from unit", ["Joule", "Kilojoule", "Megajoule", "Gigajoule", "Calorie"])
    to_unit = st.selectbox("Select to unit", ["Joule", "Kilojoule", "Megajoule", "Gigajoule", "Calorie"])
    
    if st.button("Convert"):
        result = energy_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")

