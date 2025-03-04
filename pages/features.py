import streamlit as st

st.title("Key Features")

unordered_list = [
    "Comprehensive unit conversion across multiple categories",
    "Easy-to-use interface",
    "Accurate calculations",
    "Quick and convenient conversions",
]

for item in unordered_list:
    st.write(f"* {item}")

st.write("Whether you're a student, engineer, scientist, or simply need to convert units for everyday tasks, this unit converter is the perfect tool for you!")