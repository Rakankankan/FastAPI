import streamlit as st
import requests

BASE_URL = "http://192.168.1.11:8000"  # Ganti ke IP lokal kamu

st.title("Kontrol Servo Sudut Bebas")

# Simpan nilai sebelumnya agar tidak mengirim data berkali-kali untuk nilai yang sama
if "prev_sudut" not in st.session_state:
    st.session_state.prev_sudut = 90

sudut = st.slider("Pilih sudut servo (0-180)", 0, 180, 90)

# Jika sudut berubah, kirim ke ESP32
if sudut != st.session_state.prev_sudut:
    try:
        response = requests.post(f"{BASE_URL}/arah", json={"sudut": sudut})
        if response.ok:
            st.success(f"Sudut {sudut} berhasil dikirim ke ESP32")
            st.session_state.prev_sudut = sudut  # Update nilai sebelumnya
        else:
            st.error("Gagal mengirim sudut")
    except Exception as e:
        st.error(f"Error: {e}")
