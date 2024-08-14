import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {"message": "Hello, World!"}
