import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from db import connect_db

def show():
    st.title("📊 Analytics Dashboard")

    conn = connect_db()
    df = pd.read_sql_query("""
        SELECT crop_name, COUNT(*) as demand
        FROM contracts
        GROUP BY crop_name
    """, conn)
    conn.close()

    if df.empty:
        st.warning("No contract data yet.")
    else:
        st.markdown("### 🌾 Crop Demand Overview")
        st.dataframe(df)

        # Bar chart
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(df["crop_name"], df["demand"], color='green')
        ax.set_xlabel("Crop")
        ax.set_ylabel("Contracts")
        ax.set_title("Crop Demand Analytics 📈")
        st.pyplot(fig)

        # Optional: show top 3 crops
        top = df.sort_values("demand", ascending=False).head(3)
        st.markdown("### 🏆 Top 3 Demanding Crops")
        for _, row in top.iterrows():
            st.success(f"🌾 {row['crop_name']} – {row['demand']} contracts")