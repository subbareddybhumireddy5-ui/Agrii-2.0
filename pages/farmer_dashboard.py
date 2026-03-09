import streamlit as st
from db import connect_db

st.title("Farmer Dashboard")

crop = st.text_input("Crop Name")
quantity = st.number_input("Quantity")
price = st.number_input("Price")
location = st.text_input("Location")

if st.button("Add Crop"):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO crops(farmer_id,crop_name,quantity,price,location) VALUES(%s,%s,%s,%s,%s)",
        (1,crop,quantity,price,location)
    )

    conn.commit()
    conn.close()

    st.success("Crop added successfully")