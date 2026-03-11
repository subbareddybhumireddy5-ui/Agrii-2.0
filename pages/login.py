import streamlit as st
from backend.auth import login_user

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    user = login_user(email, password)

    if user:
        st.success("Login successful")

        role = user["role"].lower()   # convert role to lowercase

        if role == "farmer":
            st.switch_page("pages/farmer_dashboard.py")

        elif role == "industry":
            st.switch_page("pages/industry_dashboard.py")

    else:
        st.error("Invalid login")