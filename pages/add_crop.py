import streamlit as st
from db import connect_db
from backend.price_ai import get_price_recommendation
import os

def show():
    st.title("🌾 Add Crop")

    farmer = st.text_input("Farmer Name")
    crop = st.text_input("Crop Name")
    quantity = st.number_input("Quantity (kg)", min_value=1)
    price = st.number_input("Price per kg", min_value=1.0)
    location = st.text_input("Location")
    image = st.file_uploader("Upload Crop Image")

    # AI Price Recommendation
    if crop:
        recommended = get_price_recommendation(crop)
        if recommended:
            st.info(f"💡 Recommended Market Price: ₹{recommended} per kg")

    if st.button("Add Crop"):
        image_path = None
        if image:
            os.makedirs("images", exist_ok=True)
            image_path = f"images/{image.name}"
            with open(image_path, "wb") as f:
                f.write(image.getbuffer())

        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO crops(farmer_name,crop_name,quantity,price,location,image) VALUES(?,?,?,?,?,?)",
            (farmer, crop, quantity, price, location, image_path)
        )
        conn.commit()
        conn.close()
        st.success("🌾 Crop added successfully!")