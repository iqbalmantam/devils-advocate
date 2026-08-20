import streamlit as st

# Custom CSS to improve aesthetics and remove sidebar dependencies
st.set_page_config(page_title="Devil's Advocate", page_icon="🔥", layout="wide")

st.markdown('''
<style>
    .main {
        background-color: #fdfbf7;
    }
    .stButton>button {
        background-color: #2b2b2b;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #e63946;
    }
    h1 {
        color: #1a1a1a;
        text-align: center;
        margin-bottom: 20px;
    }
    .instruction {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
</style>
''', unsafe_allow_html=True)

st.title("🔥 Devil's Advocate: The Strategy Stress-Tester")
st.markdown('<p class="instruction">Masukkan rencana bisnis atau ide Anda di bawah ini, dan saya akan membongkarnya sampai ke akar-akarnya.</p>', unsafe_allow_html=True)

# Main input area without sidebar
col1, col2 = st.columns([1, 1])

with col1:
    strategy_input = st.text_area("Masukkan Ide/Strategi Anda:", height=300, placeholder="Contoh: Saya ingin meluncurkan aplikasi X untuk target pasar Y dengan fitur Z...")
    
with col2:
    st.info("### Cara Kerja")
    st.write("1. Masukkan rencana Anda di kolom kiri.")
    st.write("2. Tekan tombol **'Hancurkan Ide Ini'**.")
    st.write("3. AI akan bertindak sebagai pengkritik brutal untuk menemukan celah, risiko, dan kelemahan fatal sebelum Anda melangkah lebih jauh.")
    
    intensity = st.select_slider(
        "Pilih Tingkat Kekejaman Kritik:",
        options=["Mild Skepticism", "Aggressive Critic", "Brutal Destroyer"]
    )

if st.button("Hancurkan Ide Ini"):
    if not strategy_input:
        st.warning("Mohon masukkan ide Anda terlebih dahulu!")
    else:
        st.divider()
        st.subheader("Laporan Bedah Ide (Pre-Mortem)")
        
        # Area simulasi / tempat integrasi AI logika analisis
        analysis = f"--- Analisis Berdasarkan Mode: {intensity} ---"
        st.write(analysis)
        st.write("### 1. Skenario Kegagalan Total")
        st.write("Berdasarkan input Anda, risiko terbesar adalah...")
        
        st.write("### 2. Asumsi Lemah")
        st.write("Anda terlalu percaya pada asumsi bahwa...")
        
        st.write("### 3. Deteksi Titik Buta (Blind Spots)")
        st.write("Sesuatu yang Anda lewatkan adalah...")

st.divider()
st.caption("Devil's Advocate Tool - Developed for Strategic Resilience")
