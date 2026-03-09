import streamlit as st
from db import connect_db

def show():
    st.title("🏭 Industry Dashboard")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT farmer_name, crop_name, quantity, price, location, image FROM crops")
    crops = cur.fetchall()
    conn.close()

    if not crops:
        st.warning("No crops available in marketplace yet.")
    else:
        for farmer, crop, qty, price, loc, img in crops:
            cols = st.columns([1,3])
            with cols[0]:
                if img:
                    st.image(img, width=100)
                else:
                    st.image("https://via.placeholder.com/100", width=100)
            with cols[1]:
                st.markdown(f"### 🌾 {crop}")
                st.markdown(f"👨‍🌾 **Farmer:** {farmer}")
                st.markdown(f"📦 **Quantity:** {qty} kg")
                st.markdown(f"💰 **Price:** ₹{price} /kg")
                st.markdown(f"📍 **Location:** {loc}")
            st.markdown("---")