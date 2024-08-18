from typing import List

import uvicorn
from fastapi import FastAPI, Request

from src.api.responses.investors import InvestorResponse
from src.services.investor_service import get_investors

app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {"message": "Hello, World!"}


@app.get("/investors", response_model=List[InvestorResponse])
async def home(request: Request):
    investors_response = await get_investors()
    return investors_response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
