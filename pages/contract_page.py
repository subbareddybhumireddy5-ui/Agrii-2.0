import streamlit as st
from backend.contracts import create_contract

st.title("Generate Contract")

farmer = st.number_input("Farmer ID")
industry = st.number_input("Industry ID")
crop = st.text_input("Crop")
quantity = st.number_input("Quantity")

if st.button("Generate"):

    create_contract(farmer,industry,crop,quantity)

    st.success("Contract Created")