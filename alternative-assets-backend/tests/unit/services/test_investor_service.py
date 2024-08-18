import pytest

from src.database.connection import Database
from src.services.investor_service import get_assets_by_investor_summary, get_investor_commitments, get_investors


@pytest.fixture(scope="function")
def db_session():
    """
    As we are dealing with a prepared SQLite DB. We are going to assumes our 'set' data exists, ideally we'd
    want a test fixture that creates one each time with known test data and tears it down.
    :return:
    """
    session = Database.get_session()
    yield session
    session.close()


@pytest.mark.asyncio
async def test_get_investors_multiple_mixed_data(db_session):
    response = await get_investors()

    assert len(response) == 4
    assert response[0].name == "Ioo Gryffindor fund"
    assert response[0].country_iso == "SGP"
    assert response[0].investory_type_code == "FUND_MANAGER"
    assert response[0].total_commitment == 3492000000


@pytest.mark.asyncio
async def test_get_assets_by_investor_summary(db_session):
    response = await get_assets_by_investor_summary("CWF")

    assert len(response) == 7

    # check we have an all record as the first item
    assert response[0].asset_class_code == "ALL"


@pytest.mark.asyncio
async def test_get_investor_commitments(db_session):
    response = await get_investor_commitments("CWF", "ALL")
    assert len(response) > 0

    response = await get_investor_commitments("CWF", "UNKNOWN")
    assert len(response) == 0
