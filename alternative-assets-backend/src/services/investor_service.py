from typing import List

from sqlalchemy import func
from sqlalchemy.orm import subqueryload

from src.api.responses.investors import AssetsByInvestorSummaryResponse, InvestorCommitmentsResponse, InvestorResponse
from src.database.connection import Database
from src.model.assets_under_management import AssetClass, Commitment, Investor


async def get_investors() -> List[InvestorResponse]:
    session = Database.get_session()
    # use a subquery to calculate the total commitment for each investor
    subquery = (
        session.query(Commitment.investor_code, func.sum(Commitment.amount).label("total_commitment"))
        .group_by(Commitment.investor_code)
        .subquery()
    )

    # query investors, subquery for their commitments totals
    investors = (
        session.query(Investor, subquery.c.total_commitment)
        .outerjoin(subquery, Investor.investor_code == subquery.c.investor_code)
        .options(subqueryload(Investor.country))
        .options(subqueryload(Investor.investory_type))
        .all()
    )
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


async def get_assets_by_investor_summary(investor_code: str) -> List[AssetsByInvestorSummaryResponse]:
    session = Database.get_session()

    # get all asset classes
    asset_classes = session.query(AssetClass).all()

    # initialize a list to store responses
    assets_by_investor_summary_response = []

    # calculate total commitments for each asset class for the investor
    for asset_class in asset_classes:
        total_commitment = (
            session.query(func.sum(Commitment.amount))
            .filter(Commitment.investor_code == investor_code)
            .filter(Commitment.asset_class_code == asset_class.asset_class_code)
            .scalar()
            or 0
        )

        assets_by_investor_summary_response.append(
            AssetsByInvestorSummaryResponse(
                asset_class_code=asset_class.asset_class_code,
                asset_class=asset_class.asset_class,
                total_commitment_amount=total_commitment,
            )
        )

    # calculate the total commitment across all asset classes
    total_commitment_all = (
        session.query(func.sum(Commitment.amount)).filter(Commitment.investor_code == investor_code).scalar() or 0
    )

    # add the "all" asset class response
    assets_by_investor_summary_response.insert(
        0,
        AssetsByInvestorSummaryResponse(
            asset_class_code="ALL", asset_class="All", total_commitment_amount=total_commitment_all
        ),
    )

    session.close()

    return assets_by_investor_summary_response


async def get_investor_commitments(investor_code: str, asset_class_code: str) -> List[InvestorCommitmentsResponse]:
    session = Database.get_session()

    # base query for investor commitments
    query = (
        session.query(Commitment, AssetClass.asset_class)
        .join(AssetClass, Commitment.asset_class_code == AssetClass.asset_class_code)
        .filter(Commitment.investor_code == investor_code)
    )

    # apply the asset class filter only if it's not "all"
    if asset_class_code.upper() != "ALL":
        query = query.filter(Commitment.asset_class_code == asset_class_code)

    commitments = query.all()
    session.close()

    # convert sqlalchemy results to pydantic response
    investor_commitments_response = [
        InvestorCommitmentsResponse(
            commitment_uuid=commitment.commitment_uuid,
            asset_class_code=commitment.asset_class_code,
            asset_class=asset_class,
            currency_code=commitment.currency_code,
            amount=commitment.amount,
        )
        for commitment, asset_class in commitments
    ]

    return investor_commitments_response
