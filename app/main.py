from fastapi import FastAPI
app = FastAPI(title="Books API")
@app.get("/")
def hello_world():
    return {"message": "Hello World"}
