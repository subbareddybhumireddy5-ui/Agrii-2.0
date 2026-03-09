import streamlit as st

# -------------------------------
# Import all pages from 'pages' folder
# -------------------------------
import pages.add_crop as add_crop
import pages.marketplace as marketplace
import pages.farmer_dashboard as farmer_dashboard
import pages.industry_dashboard as industry_dashboard
import pages.my_contracts as my_contracts
import pages.chat_page as chat_page
import pages.analytics_dashboard as analytics_dashboard
import pages.smart_matching as smart_matching

# -------------------------------
# Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="AgriLink", layout="wide")

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("AgriLink Navigation")
page = st.sidebar.radio(
    "Go to",
    (
        "🏡 Home",
        "🌾 Add Crop",
        "🛒 Marketplace",
        "👨‍🌾 Farmer Dashboard",
        "🏭 Industry Dashboard",
        "📑 My Contracts",
        "💬 Chat",
        "📊 Analytics",
        "🤖 Smart Matching"
    )
)

# -------------------------------
# Page Logic
# -------------------------------
if page == "🏡 Home":
    st.title("🌾 AgriLink Platform")
    st.write("""
    AgriLink connects **Farmers** and **Industries** directly for agricultural trade.
    Use the sidebar to navigate between features.
    """)
elif page == "🌾 Add Crop":
    add_crop.show()
elif page == "🛒 Marketplace":
    marketplace.show()
elif page == "👨‍🌾 Farmer Dashboard":
    farmer_dashboard.show()
elif page == "🏭 Industry Dashboard":
    industry_dashboard.show()
elif page == "📑 My Contracts":
    my_contracts.show()
elif page == "💬 Chat":
    chat_page.show()
elif page == "📊 Analytics":
    analytics_dashboard.show()
elif page == "🤖 Smart Matching":
    smart_matching.show()