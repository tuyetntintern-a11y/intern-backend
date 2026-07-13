from fastapi import FastAPI

app = FastAPI()


@app.get("/api/health")
def health_check():
    return "NGUYEN THI TUYET chao anh Nguyễn Quang Tùng"