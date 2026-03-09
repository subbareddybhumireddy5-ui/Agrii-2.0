import streamlit as st
from db import connect_db

def show():
    st.title("🤝 Smart Crop Matching")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.farmer_name, c.crop_name, c.quantity, c.price,
               ct.industry_name, ct.quantity, ct.price
        FROM crops c
        JOIN contracts ct
        ON c.crop_name = ct.crop_name
        WHERE ct.price >= c.price
    """)
    matches = cur.fetchall()
    conn.close()

    if not matches:
        st.warning("No matches found.")
    else:
        for farmer, crop, f_qty, f_price, industry, i_qty, i_price in matches:
            st.success("Match Found!")
            st.write(f"🌾 Crop: {crop}")
            st.write(f"👨‍🌾 Farmer: {farmer}")
            st.write(f"🏭 Industry: {industry}")
            st.write(f"💰 Farmer Price: ₹{f_price}")
            st.write(f"💰 Industry Offer: ₹{i_price}")
            st.write("---")