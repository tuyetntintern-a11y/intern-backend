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

@app.post("/users")
def create_user(user: dict):
    return {
        "message": "created",
        "data": user
    }
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {
        "message": "User updated",
        "id": user_id,
        "data": user
    }