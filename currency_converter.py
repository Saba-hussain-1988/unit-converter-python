import streamlit as st
import requests

def currency_converter(value, from_currency, to_currency):
    response = requests.get(f" https://v6.exchangerate-api.com/v6/f3db772d38a12744e37db10f/latest/{from_currency}")
    data = response.json()
    if 'rates' in data and to_currency in data['rates']:
        return value * data['rates'][to_currency]
    else:
        return "Invalid currency"

def currency_conversion_interface(primary_color, secondary_color):
    st.title("Currency Converter")
    st.subheader("Convert between different currencies")
    
    value = st.number_input("Enter currency value")
    from_currency = st.selectbox("Select from currency", ["USD", "EUR", "GBP", "INR", "PKR"])
    to_currency = st.selectbox("Select to currency", ["USD", "EUR", "GBP", "INR", "PKR"])
    
    if st.button("Convert"):
        result = currency_converter(value, from_currency, to_currency)
        if result != "Invalid currency":
            st.write(f"{value} {from_currency} is equal to {result} {to_currency}")
        else:
            st.error("Invalid currency")


