import streamlit as st
from backend.crops import add_crop

st.title("Farmer Dashboard")

crop = st.text_input("Crop Name")
quantity = st.number_input("Quantity")
price = st.number_input("Price")
location = st.text_input("Location")

if st.button("Add Crop"):

    add_crop(1,crop,quantity,price,location)

    st.success("Crop Added")