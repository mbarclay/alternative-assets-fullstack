import pytest

from src.database.connection import Database
from src.services.investor_service import get_investors


@pytest.fixture(scope="function")
def db_session():
    """
    We are going to assumes that the DB exists, ideally we'd want a test fixture that creates one
    each time.
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
