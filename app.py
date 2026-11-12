from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
import uvicorn

from chatbot import Chatbot
from config import MODEL_NAME, OLLAMA_BASE_URL

app = FastAPI(title="Open Source Chatbot", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chatbot = Chatbot(model_name=MODEL_NAME, base_url=OLLAMA_BASE_URL)


class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1)
    history: Optional[List[Dict[str, str]]] = []


@app.get("/api/health")
async def health():
    return {"status": "ok", "model": MODEL_NAME, "ollama_base_url": OLLAMA_BASE_URL}


@app.post("/api/chat")
async def chat(payload: ChatMessage):
    reply = await chatbot.generate(payload.message, payload.history)
    return {
        "reply": reply,
        "model": MODEL_NAME
    }


@app.get("/")
async def index():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
