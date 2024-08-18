from typing import List

import uvicorn
from fastapi import FastAPI, Request

from src.api.responses.investors import AssetsByInvestorSummaryResponse, InvestorCommitmentsResponse, InvestorResponse
from src.services.investor_service import get_assets_by_investor_summary, get_investor_commitments, get_investors

app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {"message": "Hello, World!"}


@app.get("/investors", response_model=List[InvestorResponse])
async def investors(request: Request):
    investors_response = await get_investors()
    return investors_response


@app.get("/assets-summary/{investor_code}", response_model=List[AssetsByInvestorSummaryResponse])
async def assets_summary(investor_code: str) -> List[AssetsByInvestorSummaryResponse]:
    assets_summary_response = await get_assets_by_investor_summary(investor_code)
    return assets_summary_response


@app.get(
    "/investor/{investor_code}/commitments/asset-class/{asset_class_code}",
    response_model=List[InvestorCommitmentsResponse],
)
async def investor_commitments(investor_code: str, asset_class_code: str) -> List[InvestorCommitmentsResponse]:
    investor_commitments_response = await get_investor_commitments(investor_code, asset_class_code)
    return investor_commitments_response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
