@app.get("/api/health")
def health_check():
    return {
        "status": "ok"
    }
