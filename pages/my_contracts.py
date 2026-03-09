import streamlit as st
from db import connect_db

def show():
    st.title("📑 My Contracts")

    conn = connect_db()
    cur = conn.cursor()

    # Fetch contracts from the database
    cur.execute("""
        SELECT farmer_name, crop_name, industry_name, quantity, price, status
        FROM contracts
        ORDER BY id DESC
    """)
    contracts = cur.fetchall()
    conn.close()

    if not contracts:
        st.warning("No contracts yet.")
    else:
        # Display each contract as a card
        for farmer, crop, industry, qty, price, status in contracts:
            st.markdown(f"### 🌾 {crop} Contract")
            st.markdown(f"👨‍🌾 **Farmer:** {farmer}")
            st.markdown(f"🏭 **Industry:** {industry}")
            st.markdown(f"📦 **Quantity:** {qty}")
            st.markdown(f"💰 **Price:** ₹{price}")

            # Color-coded status
            if status.lower() == "approved":
                st.success(f"✅ Status: {status}")
            elif status.lower() == "pending":
                st.warning(f"⏳ Status: {status}")
            elif status.lower() == "rejected":
                st.error(f"❌ Status: {status}")
            else:
                st.info(f"ℹ️ Status: {status}")

            st.markdown("---")  # Divider between contracts