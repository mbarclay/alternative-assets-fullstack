import os
import sqlite3

import pandas as pd

from config import settings
from src.database.connection import Database


def create_database(sql_path: str, db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # read the sql file
    with open(sql_path, "r") as sql_file:
        sql_script = sql_file.read()

    try:
        cursor.executescript(sql_script)
        print(f"Database '{db_path}' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.commit()
        conn.close()


def populate_database():
    session = Database.get_session()

    # read our data csv into a pandas data frame
    df = pd.read_csv("data.csv")

    # insert our various entities
    insert_investory_types(df)
    insert_countries(df)
    insert_asset_classes(df)
    insert_investors(df)

    session.close()


def column_to_unique_list(df: pd.DataFrame, column: str) -> [str]:
    return df[column].unique().tolist()


def insert_investory_types(df: pd.DataFrame):
    investory_types = column_to_unique_list(df, "Investory Type")
    print(investory_types)


def insert_countries(df: pd.DataFrame):
    countries = column_to_unique_list(df, "Investor Country")
    print(countries)


def insert_asset_classes(df: pd.DataFrame):
    assets_classes = column_to_unique_list(df, "Commitment Asset Class")
    print(assets_classes)


def insert_investors(df: pd.DataFrame):
    investors = column_to_unique_list(df, "Investor Name")
    print(investors)


if __name__ == "__main__":
    # define the sql file path and the database name
    sql = "assets_under_management.sql"
    db = f"../{settings.database_name}.sqlite"

    # if the database already exists, delete it, we will recreate it
    if os.path.exists(db):
        os.remove(db)

    # create the database
    create_database(sql, db)

    # populate the database
    populate_database()
