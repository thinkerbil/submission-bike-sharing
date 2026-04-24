import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set konfigurasi halaman
st.set_page_config(page_title="Bikeshare Data Dashboard 🚲", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "main_data.csv")
    
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# --- SIDEBAR FILTER ---
with st.sidebar:
    st.sidebar.image("https://raw.githubusercontent.com/thinkerbil/submission-bike-sharing/main/logo.png", use_container_width=True)
    st.title("Filter Panel")
    
    # Filter rentang waktu
    min_date = main_df["dteday"].min()
    max_date = main_df["dteday"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter dataframe berdasarkan sidebar
filtered_df = main_df[(main_df["dteday"] >= str(start_date)) & 
                       (main_df["dteday"] <= str(end_date))]

# --- HEADER ---
st.title("🚲 Capital Bikeshare: Business Performance Dashboard")
st.markdown("Dashboard ini menyajikan analisis mendalam tentang perilaku penyewa sepeda berdasarkan waktu, cuaca, dan profil hari.")

# --- MAIN METRICS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_rentals = filtered_df['cnt'].sum()
    st.metric("Total Peminjaman", value=f"{total_rentals:,}")
with col2:
    casual_rentals = filtered_df['casual'].sum()
    st.metric("Penyewa Casual", value=f"{casual_rentals:,}")
with col3:
    reg_rentals = filtered_df['registered'].sum()
    st.metric("Penyewa Terdaftar", value=f"{reg_rentals:,}")
with col4:
    avg_temp = f"{filtered_df['temp'].mean() * 41:.1f}°C"
    st.metric("Rata-rata Suhu", value=avg_temp)

st.divider()

# --- PERTANYAAN 1: TREN BULANAN ---
st.subheader("Pertumbuhan Tren Bulanan (2011 vs 2012)")
monthly_df = filtered_df.resample(rule='M', on='dteday').agg({"cnt": "sum"}).reset_index()
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(monthly_df["dteday"], monthly_df["cnt"], marker='o', linewidth=2, color="#396EB0")
ax.set_title("Jumlah Penyewaan Sepeda per Bulan", loc="center", fontsize=18)
st.pyplot(fig)

# --- PERTANYAAN 2 & 4: CUACA & HARI LIBUR ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Dampak Kondisi Cuaca")
    weather_df = filtered_df.groupby("weathersit").cnt.mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#396EB0", "#DADADA", "#DADADA", "#DADADA"]
    sns.barplot(x="weathersit", y="cnt", data=weather_df, palette=colors, ax=ax)
    ax.set_xticklabels(['Cerah', 'Mendung', 'Hujan/Salju Ringan', 'Cuaca Ekstrem'])
    st.pyplot(fig)

with col_b:
    st.subheader("Hari Libur vs Hari Biasa")
    holiday_df = filtered_df.groupby("holiday").cnt.mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="holiday", y="cnt", data=holiday_df, palette=["#396EB0", "#FC9918"], ax=ax)
    ax.set_xticklabels(['Hari Biasa', 'Hari Libur'])
    st.pyplot(fig)

# --- PERTANYAAN 3: POLA JAM (LENGKAP DENGAN MUSIM) ---
st.subheader("Pola Penyewaan Berdasarkan Jam & Hari Kerja")
fig, ax = plt.subplots(figsize=(16, 7))
sns.pointplot(data=filtered_df, x='hr', y='cnt', hue='workingday', palette={0: "#FC9918", 1: "#396EB0"}, ax=ax)
ax.set_title("Distribusi Penyewaan Per Jam (0: Akhir Pekan, 1: Hari Kerja)")
st.pyplot(fig)

# --- PERTANYAAN 5: ANALISIS RFM (TIME SEGMENTATION) ---
st.subheader("Analisis Performa Berdasarkan Hari (RFM Terapan)")
# Kita sederhanakan untuk dashboard: Melihat hari dengan volume tertinggi
top_days = filtered_df.sort_values(by="cnt", ascending=False).head(10)
st.write("10 Hari dengan Volume Penyewaan Tertinggi:")
st.table(top_days[['dteday', 'cnt', 'temp', 'weathersit']].head(5))

# --- FOOTER ---
st.caption('Copyright © 2026 - Bike Sharing Analysis Project')