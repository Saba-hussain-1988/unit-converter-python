import streamlit as st

def pressure_converter(value, from_unit, to_unit):
    if from_unit == "Pascal" and to_unit == "Bar":
        return value / 100000
    elif from_unit == "Pascal" and to_unit == "Atmosphere":
        return value / 101325
    elif from_unit == "Pascal" and to_unit == "Pounds per square inch":
        return value / 6894.76
    elif from_unit == "Bar" and to_unit == "Pascal":
        return value * 100000
    elif from_unit == "Bar" and to_unit == "Atmosphere":
        return value * 0.9869
    elif from_unit == "Bar" and to_unit == "Pounds per square inch":
        return value * 14.5038
    elif from_unit == "Atmosphere" and to_unit == "Pascal":
        return value * 101325
    elif from_unit == "Atmosphere" and to_unit == "Bar":
        return value * 1.01325
    elif from_unit == "Atmosphere" and to_unit == "Pounds per square inch":
        return value * 14.6959
    elif from_unit == "Pounds per square inch" and to_unit == "Pascal":
        return value * 6894.76
    elif from_unit == "Pounds per square inch" and to_unit == "Bar":
        return value / 14.5038
    elif from_unit == "Pounds per square inch" and to_unit == "Atmosphere":
        return value / 14.6959
    else:
        return "Invalid units"

def pressure_conversion_interface():
    st.title("Pressure Converter")
    st.subheader("Convert between different units of pressure")    
    value = st.number_input("Enter pressure value")
    from_unit = st.selectbox("Select from unit", ["Pascal", "Bar", "Atmosphere", "Pounds per square inch"])
    to_unit = st.selectbox("Select to unit", ["Pascal", "Bar", "Atmosphere", "Pounds per square inch"])
    
    if st.button("Convert"):
        result = pressure_converter(value, from_unit, to_unit)
        if result != "Invalid units":
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Invalid units")


