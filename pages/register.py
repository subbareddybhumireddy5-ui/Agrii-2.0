import streamlit as st
from backend.auth import register_user

st.title("Register")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password",type="password")

role = st.selectbox("Role",["Farmer","Industry"])

if st.button("Register"):

    register_user(name,email,password,role)

    st.success("Registration successful")