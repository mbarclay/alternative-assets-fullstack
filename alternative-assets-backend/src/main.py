from typing import List

import uvicorn
from fastapi import FastAPI, Request
from sqlalchemy import func
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import joinedload, subqueryload

from src.api.responses.investors import InvestorResponse
from src.database.connection import Database
from src.model.assets_under_management import Investor, Commitment

app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {"message": "Hello, World!"}


@app.get("/investors", response_model=List[InvestorResponse])
async def home(request: Request):
    session = Database.get_session()

    # use a subquery to calculate the total commitment for each investor
    subquery = session.query(
        Commitment.investor_code,
        func.sum(Commitment.amount).label('total_commitment')
    ).group_by(Commitment.investor_code).subquery()

    # query investors, subquery for their commitments totals
    investors = (session.query(
        Investor,
        subquery.c.total_commitment
    ).outerjoin(
        subquery, Investor.investor_code == subquery.c.investor_code
    ).options(
        subqueryload(Investor.country)
    ).options(
        subqueryload(Investor.investory_type)
    ).all())

    session.close()

    # convert sqlalchemy to our pydantic response
    investors_response = [
        InvestorResponse(
            investor_code=investor.investor_code,
            name=investor.name,
            country_iso=investor.country.iso if investor.country else None,
            country_name=investor.country.name if investor.country else None,
            investory_type_code=investor.investory_type_code,
            investory_type=investor.investory_type.investory_type if investor.investory_type else None,
            total_commitment=total_commitment if total_commitment else 0,
            added_epoch=investor.added_epoch,
        )
        for investor, total_commitment in investors
    ]

    return investors_response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
