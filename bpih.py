import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objs as go

st.set_page_config(layout="wide")

# ----- Horizontal Navigation Menu -----
selected = option_menu(
    menu_title=None,  # Hide the title
    options=["Dashboard", "Regional Analysis", "AI Predictions", "Data Documentation"],
    icons=["bar-chart", "globe", "robot", "file-earmark-text"],
    menu_icon="cast",
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#ffffff"},
        "icon": {"color": "#8e44ad", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#e8e8e8"},
    },
)
