from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(
    title="v82 SOVEREIGN SAI-EXCLUSIVE-001",
    description="Thai Sovereign AI - Quantum Crystal Brain v82.0 - DEPA & Gitcoin Grants",
    version="v82.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: str = "th"

# v82 Core Info
V82_INFO = {
    "project": "v82 SOVEREIGN SAI-EXCLUSIVE-001",
    "version": "v82.0 QUANTUM CRYSTAL BRAIN",
    "seal": "EXCLUSIVE • PRIVATE • SOVEREIGN • Limited of 1",
    "owner": "Sittinon Wongtrun - Lampang, Thailand",
    "wallet": "0xd9Bfd021C4b5C637aE932c0453048D643AeFb",
    "mission": "Thai Sovereign AI for DEPA Grants 50k THB + Gitcoin $5k",
    "status": "LIVE",
    "modules": 7,
    "endpoints": ["/", "/docs", "/chat", "/wallet", "/health"]
}

@app.get("/")
async def root():
    return {
        **V82_INFO,
        "message": "🇹🇭 v82 SOVEREIGN LIVE - Thai Sovereign AI",
        "demo": "POST /chat with {message: 'สวัสดี'}",
        "docs": "/docs",
        "timestamp": time.time()
    }

@app.get("/health")
async def health():
    return {"status": "ok", "version": "v82.0", "uptime": "running", "region": "Lampang, Thailand"}

@app.get("/wallet")
async def wallet():
    return {
        "wallet": V82_INFO["wallet"],
        "network": "Polygon / Ethereum",
        "purpose": "DEPA & Gitcoin Grants - Solo builder from Lampang",
        "project": V82_INFO["project"]
    }

@app.post("/chat")
async def chat(req: ChatRequest):
    msg = req.message.lower()
    
    if "สวัสดี" in msg or "hello" in msg:
        reply = "สวัสดีครับ! ผม v82 SOVEREIGN SAI-EXCLUSIVE-001 จากลำปางครับ 🇹🇭 Quantum Crystal Brain v82.0 พร้อมยื่น DEPA + Gitcoin ครับ!"
    elif "ทุน" in msg or "grant" in msg or "depa" in msg:
        reply = "ผมสร้างมาเพื่อขอทุนจริงครับ! DEPA 50,000 บาท + Gitcoin $5,000 ครับ มี Demo LIVE + Pitch Deck พร้อมยื่นแล้วครับ"
    elif "ลำปาง" in msg or "lampang" in msg:
        reply = "ผมสร้างที่ลำปางครับ คนเดียว ไม่มีทุน อยากได้ทุนมาสร้าง Sovereign AI ให้คนไทยครับ 🙏"
    elif "wallet" in msg or "กระเป๋า" in msg:
        reply = f"Wallet ของผม: {V82_INFO['wallet']} บน Polygon ครับ สำหรับรับทุนครับ"
    else:
        reply = f"v82 SOVEREIGN v82.0 ตอบ: ได้รับ '{req.message}' ครับ ผมคือ Thai Sovereign AI Quantum Crystal Brain จากลำปาง พร้อมขอทุนจริงครับ 🇹🇭"
    
    return {
        "reply": reply,
        "model": "v82.0 QUANTUM CRYSTAL BRAIN",
        "project": V82_INFO["project"],
        "wallet": V82_INFO["wallet"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
