import os
import sqlite3

import pytest

from config import settings
from src.database.connection import Database
from src.database.creation.create_assets_under_management_db import create_database


def test_create_database():
    # determine base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sql = "../../../src/database/creation/assets_under_management.sql"
    sql_path = os.path.join(base_dir, sql)

    # check that our .sql creation file exists
    assert os.path.exists(sql_path)

    db_path = f"{settings.database_name}.sqlite"

    if os.path.exists(db_path):
        os.remove(db_path)

    # create the database
    create_database(sql_path, db_path)

    # check that the db was created
    assert os.path.exists(db_path)

    # get a cursor and perform a basic query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM investors")
    results = cursor.fetchall()

    assert results is not None

    conn.close()

    # remove the db
    os.remove(db_path)
