from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS biar bisa diakses dari Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ESP32_URL = "http://192.168.1.11"  # IP lokal ESP32 kamu

@app.post("/arah")
async def kirim_sudut(request: Request):
    data = await request.json()
    sudut = data.get("sudut")

    try:
        # Kirim request ke ESP32
        resp = requests.post(f"{ESP32_URL}/arah", json={"sudut": sudut}, timeout=2)
        return {"status": "ok", "response": resp.text}
    except Exception as e:
        return {"status": "gagal", "error": str(e)}
