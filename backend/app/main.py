from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.chat import ask_aura

app = FastAPI(title="AURA API", version="0.1.0")

class ChatRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "aura-api"}

@app.get("/")
def root():
    return {"message": "AURA is running"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    answer = ask_aura(request.question)
    return {"response": answer}