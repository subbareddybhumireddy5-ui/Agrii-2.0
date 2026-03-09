import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Nearby Farmers")

m = folium.Map(location=[17.3850,78.4867],zoom_start=6)

folium.Marker(
    [17.3850,78.4867],
    popup="Farmer Location"
).add_to(m)

st_folium(m,width=700)