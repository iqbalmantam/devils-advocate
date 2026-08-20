import streamlit as st
from google import genai

# Konfigurasi halaman
st.set_page_config(page_title="Devil's Advocate", page_icon="🔥", layout="wide")

# Custom CSS agar tampilan bersih tanpa sidebar
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
st.markdown('<p class="instruction">Masukkan rencana bisnis atau ide Anda di bawah ini, dan biarkan AI membongkarnya sampai ke akar-akarkanya.</p>', unsafe_allow_html=True)

# Ambil API key dari st.secrets (pastikan diset di Streamlit Cloud Secrets)
api_key = st.secrets.get("GEMINI_API_KEY")

# Layout utama tanpa sidebar
col1, col2 = st.columns([1, 1])

with col1:
    strategy_input = st.text_area("Masukkan Ide/Strategi Anda:", height=300, placeholder="Contoh: Saya ingin meluncurkan aplikasi X untuk target pasar Y dengan fitur Z...")
    
with col2:
    st.info("### Cara Kerja")
    st.write("1. Masukkan rencana Anda di kolom kiri.")
    st.write("2. Atur tingkat kekejaman kritik di bawah.")
    st.write("3. Tekan tombol **'Hancurkan Ide Ini'**.")
    
    intensity = st.select_slider(
        "Pilih Tingkat Kekejaman Kritik:",
        options=["Mild Skepticism", "Aggressive Critic", "Brutal Destroyer"]
    )

if st.button("Hancurkan Ide Ini"):
    if not strategy_input:
        st.warning("Mohon masukkan ide Anda terlebih dahulu!")
    elif not api_key:
        st.error("API Key Gemini belum disetel di Streamlit Secrets (`GEMINI_API_KEY`)!")
    else:
        with st.spinner("Sedang membedah dan menghancurkan asumsi Anda..."):
            try:
                # Inisialisasi klien Gemini
                client = genai.Client(api_key=api_key)
                
                # Atur prompt berdasarkan tingkat kekejaman
                system_instruction = f"""
                Anda adalah 'Devil's Advocate' yang bertindak dengan level kekejaman: {intensity}.
                Tugas Anda adalah melakukan analisis pre-mortem secara brutal, skeptis, dan objektif terhadap rencana atau strategi yang diberikan pengguna.
                Berikan analisis dalam format bahasa Indonesia yang tajam dan terstruktur ke dalam bagian berikut:
                1. Skenario Kegagalan Total (Worst-case scenario)
                2. Asumsi Lemah (Flawed assumptions yang disembunyikan pembuat ide)
                3. Deteksi Titik Buta (Blind spots dan risiko tersembunyi)
                4. Saran Perbaikan / Mitigasi
                """
                
                # Panggil model Gemini
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=strategy_input,
                    config={
                        'system_instruction': system_instruction,
                        'temperature': 0.7,
                    }
                )
                
                st.divider()
                st.subheader("Laporan Bedah Ide (Pre-Mortem)")
                st.write(response.text)
                
            except Exception as e:
                st.error(fTerjadi kesalahan saat menghubungi API Gemini: {e}")

st.divider()
st.caption("Devil's Advocate Tool - Powered by Google Gemini & Streamlit")
