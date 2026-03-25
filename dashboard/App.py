import streamlit as st

import os

if not os.path.exists("olist.db"):
    import init_db

st.set_page_config(
	page_title="Brazilian E-Commerce Dashboard",
	layout="wide"
)

st.title("Olist E-Commerce Dashboard")

st.markdown("""
Welcome to the analytics dashboard.

Use the sidebar to navigate:
- Executive Overview
- Product Intelligence
- Customer Intelligence
- Customer Distribution Map
- Cohort Analysis

""")