from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from watermark_engine import NeuralWatermarkEngine

app = FastAPI(title="AI-Driven Anti-Piracy Dashboard")

# ✅ ENABLE CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (safe for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = NeuralWatermarkEngine()

@app.get("/")
def root():
    return {"message": "AI Anti-Piracy Dashboard is running"}

@app.post("/embed-watermark")
def embed(video_name: str, watermark_id: str):
    return engine.embed_watermark(video_name, watermark_id)

@app.post("/extract-watermark")
def extract(leaked_video_name: str):
    return engine.extract_watermark(leaked_video_name)
