from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "مرحبا بك في سوق الرقة"}
