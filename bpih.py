import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# ----- Simulasi Navigasi -----
st.set_page_config(layout="wide")
menu = ["Dashboard", "Regional Analysis", "AI Predictions", "Data Documentation"]
selected = st.sidebar.radio("Navigation", menu)
