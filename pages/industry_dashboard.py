import streamlit as st

st.set_page_config(layout="wide")

st.title("🏭 Industry Dashboard")

menu = st.sidebar.selectbox(
    "Industry Menu",
    ["Dashboard", "View Farmer Crops", "Create Contract", "Analytics", "Logout"]
)

# Dashboard
if menu == "Dashboard":

    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Available Crops", "120")

    with col2:
        st.metric("Active Contracts", "10")

    with col3:
        st.metric("Farmers Connected", "35")


# View Crops
elif menu == "View Farmer Crops":

    st.subheader("Farmer Crops")

    st.table({
        "Farmer": ["Ravi", "Suresh", "Mahesh"],
        "Crop": ["Rice", "Tomato", "Corn"],
        "Quantity": ["500 kg", "800 kg", "1200 kg"]
    })


# Create Contract
elif menu == "Create Contract":

    st.subheader("Create Contract")

    crop = st.text_input("Crop Name")
    quantity = st.number_input("Required Quantity")

    if st.button("Create Contract"):
        st.success("Contract Created")


# Analytics
elif menu == "Analytics":

    st.subheader("Market Analytics")

    st.write("Demand and supply insights")


# Logout
elif menu == "Logout":

    st.switch_page("pages/login.py")