# 🚲 Capital Bikeshare: Business Performance Dashboard
![Preview Dashboard](./dashboard/preview_dashboard.jpeg)

Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset bike-sharing guna memahami pola penggunaan sepeda berdasarkan berbagai faktor seperti waktu, kondisi cuaca, dan profil pengguna (kasual vs terdaftar). Hasil analisis ini memberikan wawasan strategis untuk optimasi manajemen armada dan strategi pemasaran.

Dashboard interaktif ini memungkinkan eksplorasi dinamis terhadap tren penyewaan berdasarkan berbagai parameter waktu dan kondisi lingkungan.

## 🚀 Fitur Utama
- <b>Data Wrangling:</b> Proses pembersihan data, penanganan nilai hilang, dan penyesuaian tipe data untuk memastikan akurasi analisis.
- <b>Exploratory Data Analysis (EDA):</b> Identifikasi tren musiman, harian, dan pengaruh variabel eksternal (suhu, kelembapan) terhadap jumlah penyewaan.
- <b>Analisis Statistik:</b> Uji normalitas (Shapiro-Wilk) dan analisis varians untuk memvalidasi karakteristik data secara formal.
- <b>RFM Analysis (2012):</b> Segmentasi data berdasarkan Recency, Frequency, dan Monetary (Volume) untuk memahami tingkat maturitas layanan di tahun puncak.
- <b>Interactive Dashboard:</b> Visualisasi dinamis menggunakan Streamlit dengan filter rentang waktu untuk eksplorasi data secara real-time.

## 📂 Struktur Proyek
- `dashboard/`: Berisi file utama untuk dashboard (`dashboard.py`, `main_data.csv`, dan aset gambar).
- `data/`: Dataset mentah (day.csv & hour.csv).
- `notebook.ipynb`: Proses dokumentasi analisis data mulai dari Wrangling, EDA, RFM Analysis, hingga Visualisasi Data dan Explanation Data Analysis.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.

## 🛠️ Teknonologi yang Digunakan
- <b>Bahasa Pemrograman:</b> Python
- <b>Library Analisis:</b> Pandas, NumPy
- <b>Visualisasi:</b> Matplotlib, Seaborn
- <b>Deployment Dashboard:</b> Streamlit

## 🛠️ Persiapan Lingkungan (Setup Environment)

### Setup Environment - Anaconda/Conda
```
conda create --name bike-sharing-ds python=3.9
conda activate bike-sharing-ds
pip install -r requirements.txt
```

### Setup Environment - Terminal/Shell
```
# Masuk ke direktori proyek
cd proyek_analisis_data

# Membuat virtual environment
python -m venv venv

# Aktivasi venv (Windows)
venv\Scripts\activate

# Aktivasi venv (Mac/Linux)
source venv/bin/activate

# Install library yang dibutuhkan
pip install -r requirements.txt
```

### Run Stremlit App
streamlit run dashboard/dashboard.py

## Link Dashboard (Streamlit Cloud)
Anda juga dapat mengakses versi live dari dashboard ini melalui tautan berikut:
👉 [Dashboard Bike Share Analysis](https://bike-share-analysis-nabila-najwa-husna.streamlit.app/)

## 📊 Analisis Singkat
- <b>Pola Komuter:</b> Terdeteksi lonjakan penggunaan pada jam 08.00 dan 17.00 di hari kerja, menunjukkan ketergantungan pekerja pada layanan ini.
- <b>Sensitivitas Cuaca:</b> Cuaca buruk (hujan/salju ringan) menurunkan rata-rata penyewaan hingga lebih dari 50% dibandingkan kondisi cerah.
- <b>Dominasi Pengguna:</b> Pengguna terdaftar (registered) memberikan kontribusi dominan (korelasi 0.94) terhadap total transaksi harian.
- <b>Pertumbuhan Layanan:</b> Tahun 2012 menunjukkan performa puncak dengan rata-rata harian mencapai 6.000 - 8.000 penyewaan.

