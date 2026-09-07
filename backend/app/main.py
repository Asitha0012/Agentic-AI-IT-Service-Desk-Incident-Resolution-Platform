from fastapi import FastAPI

app = FastAPI(title="AURA API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "aura-api"}

@app.get("/")
def root():
    return {"message": "AURA is running"}