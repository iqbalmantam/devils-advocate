import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Devil's Advocate", page_icon="🔥", layout="wide")

# CSS untuk menyembunyikan header/ikon bawaan Streamlit (GitHub, Share, Menu, dll)
st.markdown("""
    <style>
    [data-testid="stHeader"] {
        display: none;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
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
    </style>
""", unsafe_allow_html=True)

# Ambil API Key Gemini dari Streamlit Secrets
gemini_key = st.secrets.get("GEMINI_API_KEY") or (st.secrets.get("general") or {}).get("GEMINI_API_KEY")
if gemini_key:
    genai.configure(api_key=gemini_key)

st.title("🔥 Devil's Advocate: The Strategy Stress-Tester")
st.markdown("Asisten cerdas yang bertindak sebagai pengkritik brutal untuk menguji ketahanan strategi dan ide bisnis Anda.")

# Layout utama tanpa sidebar (menggunakan 2 kolom berdampingan)
col1, col2 = st.columns([1, 1])

with col1:
    strategy_input = st.text_area("Masukkan Ide/Strategi Anda:", height=300, placeholder="Contoh: Saya ingin meluncurkan aplikasi X untuk target pasar Y dengan fitur Z...")
    
with col2:
    st.info("### Cara Kerja")
    st.write("1. Masukkan rencana Anda di kolom kiri.")
    st.write("2. Pilih tingkat kekejaman kritik di bawah.")
    st.write("3. Tekan tombol **'Hancurkan Ide Ini'**.")
    
    intensity = st.select_slider(
        "Pilih Tingkat Kekejaman Kritik:",
        options=["Mild Skepticism", "Aggressive Critic", "Brutal Destroyer"]
    )

if st.button("Hancurkan Ide Ini"):
    if not strategy_input:
        st.warning("Mohon masukkan ide atau strategi Anda terlebih dahulu!")
    elif not gemini_key:
        st.error("API Key Gemini belum disetel di Streamlit Secrets (`GEMINI_API_KEY`)!")
    else:
        with st.spinner("⏳ Sedang membedah dan menghancurkan asumsi Anda..."):
            try:
                # Menggunakan model gemini-3.6-flash yang terbukti berhasil
                model = genai.GenerativeModel('gemini-3.6-flash')
                
                full_prompt = f"""
                Anda adalah 'Devil's Advocate' yang bertindak dengan level kekejaman: {intensity}.
                Tugas Anda adalah melakukan analisis pre-mortem secara brutal, skeptis, dan objektif terhadap rencana atau strategi berikut.
                
                Rencana / Ide Pengguna:
                {strategy_input}
                
                Berikan analisis dalam format bahasa Indonesia yang tajam dan terstruktur ke dalam bagian berikut:
                1. Skenario Kegagalan Total (Worst-case scenario)
                2. Asumsi Lemah (Flawed assumptions yang disembunyikan pembuat ide)
                3. Deteksi Titik Buta (Blind spots dan risiko tersembunyi)
                4. Saran Perbaikan / Mitigasi
                """
                
                response = model.generate_content(full_prompt)
                
                st.divider()
                st.subheader("Laporan Bedah Ide (Pre-Mortem)")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungi API Gemini: {e}")

# Watermark bagian bawah
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 13px;'>Developed by <b>iqbalmantam</b></p>", unsafe_allow_html=True)
