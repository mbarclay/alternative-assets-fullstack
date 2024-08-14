from typing import List

import uvicorn
from fastapi import FastAPI, Request
from sqlalchemy.orm import joinedload

from src.api.responses.investors import InvestorResponse
from src.database.connection import Database
from src.model.assets_under_management import Investor

app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {"message": "Hello, World!"}


@app.get("/investors", response_model=List[InvestorResponse])
async def home(request: Request):
    session = Database.get_session()
    investors = session.query(Investor).options(joinedload(Investor.country)).all()
    session.close()

    investor_responses = [
        InvestorResponse(
            investor_code=inv.investor_code,
            name=inv.name,
            country_iso=inv.country.iso,
            country_name=inv.country.name
        )
        for inv in investors
    ]

    return investor_responses


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
