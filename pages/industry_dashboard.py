import streamlit as st
import pandas as pd
from db import connect_db

st.title("Available Crops")

conn = connect_db()

df = pd.read_sql("SELECT * FROM crops",conn)

st.dataframe(df)

conn.close()