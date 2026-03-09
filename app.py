import streamlit as st
from db import create_tables

create_tables()

st.set_page_config(page_title="AgriLink", layout="wide")

st.title("🌾 AgriLink Platform")

st.write("""
AgriLink connects **Farmers** and **Industries** directly for agricultural trade.
""")

st.success("Use the sidebar to navigate the system")