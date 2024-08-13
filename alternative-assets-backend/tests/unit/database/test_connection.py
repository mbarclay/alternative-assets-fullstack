import pytest
from sqlalchemy.engine import Engine

from src.database.connection import Database


@pytest.fixture(scope="function")
def db_session():
    session = Database.get_session()
    yield session
    session.close()


def test_get_session(db_session):
    assert isinstance(db_session.bind.engine, Engine)
