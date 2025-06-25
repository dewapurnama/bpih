import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objs as go

st.set_page_config(layout="wide")

tab0, tab1, tab2, tab3 = st.tabs(["Dashboard", "Regional Analysis", "AI Predictions", "Data Documentation"])

tab0.subheader(":bar_chart: Dashboard Realisasi SBN DJPPR")
tab0.markdown(
    "<h1 style='font-size:25px;'>📊 Data Historis dan Proyeksi BPIH</h1>",
    unsafe_allow_html=True
)


