import streamlit as st
from backend.auth import login_user

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password",type="password")

if st.button("Login"):

    user = login_user(email,password)

    if user:
        st.success("Login successful")
    else:
        st.error("Invalid login")