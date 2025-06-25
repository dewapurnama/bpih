import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pandas as pd

st.set_page_config(layout="wide")

tab0, tab1, tab2, tab3 = st.tabs(["Dashboard", "Regional Analysis", "AI Predictions", "Data Documentation"])

# ----- Statistik -----
col1, col2, col3, col4 = tab0.columns(4)
with col1:
    tab0.markdown("#### 🔥 Biaya Haji 2025")
    tab0.metric("Rp", "52.000.000", "+9.5%")
    
tab0.markdown(
    "<h1 style='font-size:25px;'>📊 Data Historis dan Proyeksi BPIH</h1>",
    unsafe_allow_html=True
)
df = st.file_uploader("Upload Data Terbaru Disini", type=['xls', 'xlsx'])
if df is not None:
    df = pd.read_excel(df)

    # Group by year, take mean of bipih and nm
    df["tahun"] = df["tahun"].astype(str)
    df_grouped = df.groupby("tahun")[["bipih", "nm"]].mean().reset_index()

    # Optional: convert values to millions for readability
    df_grouped["bipih_mio"] = df_grouped["bipih"] / 1e6
    df_grouped["nm_mio"] = df_grouped["nm"] / 1e6
    df_grouped["tahun"] = df_grouped["tahun"].astype(str)
    df_grouped["total_mio"] = df_grouped["bipih_mio"] + df_grouped["nm_mio"]
    
    fig = go.Figure()
    
    # NM bar
    fig.add_trace(go.Bar(
        x=df_grouped["tahun"],
        y=df_grouped["nm_mio"],
        name="NM",
        text=[f'{x:.2f} jt' for x in df_grouped["nm_mio"]],
        textposition='auto',
        textangle=0,
        textfont=dict(size=10, color="white"),
        marker_color="#e07b39"
    ))
    
    # Bipih bar
    fig.add_trace(go.Bar(
        x=df_grouped["tahun"],
        y=df_grouped["bipih_mio"],
        name="Bipih",
        text=[f'{x:.2f} jt' for x in df_grouped["bipih_mio"]],
        textposition='inside',  textangle=0,
        marker_color="#4a8db7"
    ))
    
    # Total label outside (on top of full stacked bar)
    fig.add_trace(go.Scatter(
        x=df_grouped["tahun"],
        y=df_grouped["total_mio"] + 2,  # Shift label above bar
        mode='text',
        text=[f'{x:.2f} jt' for x in df_grouped["total_mio"]],
        textfont=dict(size=10, color="black"),
        showlegend=False
    ))
    
    fig.update_layout(
        barmode='stack',
        title=dict(
            text="Komponen BPIH (Dalam Juta)",
            x=0.5,
            xanchor='center',
            font=dict(size=18)
        ),
        xaxis=dict(
            title="Tahun",
            tickmode='linear'
        ),
        yaxis_title="Rata-rata (Jutaan Rp)",
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.05,
            xanchor='center',
            x=0.5,
            title=None
        ),
        template="seaborn"
    )
    
    st.plotly_chart(fig, use_container_width=True, height=200)
