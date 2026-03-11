import streamlit as st

st.set_page_config(layout="wide")

st.title("👨‍🌾 Farmer Dashboard")

menu = st.sidebar.selectbox(
    "Farmer Menu",
    ["Dashboard", "Add Crop", "Industry Demand", "My Contracts", "Logout"]
)

# Dashboard
if menu == "Dashboard":

    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Crops Listed", "4")

    with col2:
        st.metric("Active Contracts", "2")

    with col3:
        st.metric("Pending Requests", "1")


# Add Crop
elif menu == "Add Crop":

    st.subheader("Add Crop")

    crop = st.text_input("Crop Name")
    quantity = st.number_input("Quantity (kg)")
    price = st.number_input("Expected Price")

    if st.button("Add Crop"):
        st.success("Crop Added Successfully")


# Industry Demand
elif menu == "Industry Demand":

    st.subheader("Industry Crop Demand")

    st.write("List of crops industries are requesting.")

    st.table({
        "Crop": ["Rice", "Wheat", "Corn"],
        "Quantity Needed": ["2000 kg", "1500 kg", "3000 kg"]
    })


# My Contracts
elif menu == "My Contracts":

    st.subheader("My Contracts")

    st.write("Contracts with industries will appear here.")


# Logout
elif menu == "Logout":

    st.switch_page("pages/login.py")