from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path


app = FastAPI()


@app.get("/")
def home():
    content = Path("app/templates/index.html").read_text(
        encoding="utf-8"
    )
    return HTMLResponse(content=content)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "Backend server is running"
    }