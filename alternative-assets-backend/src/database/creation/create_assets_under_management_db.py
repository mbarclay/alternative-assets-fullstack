import os
import sqlite3

import pandas as pd
import pycountry

from config import settings
from src.database.connection import Database
from src.model.assets_under_management import AssetClass, Commitment, Country, Investor, InvestoryType
from src.utilities.epoch import date_string_to_epoch


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
    # determine base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # read our data csv into a pandas data frame
    assets_under_management_csv_path = os.path.join(base_dir, "creation", "assets_under_management.csv")
    df = pd.read_csv(assets_under_management_csv_path)

    # renaming the columns to pythonic variable names
    df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("[^a-z0-9_]", "")

    # insert our various entities
    insert_investory_types(df)
    insert_countries(df)
    insert_asset_classes(df)
    insert_investors(df)
    insert_commitments(df)


def column_to_unique_list(df: pd.DataFrame, column: str) -> [str]:
    return df[column].unique().tolist()


def insert_investory_types(df: pd.DataFrame):
    session = Database.get_session()
    investory_type_list = column_to_unique_list(df, "investory_type")

    for investory_type_category in investory_type_list:
        investory_type_code = investory_type_category.upper().replace(" ", "_")
        investory_type = InvestoryType(investory_type_code=investory_type_code, investory_type=investory_type_category)
        session.add(investory_type)
        session.commit()

    session.close()


def insert_countries(df: pd.DataFrame):
    session = Database.get_session()
    countries_list = column_to_unique_list(df, "investor_country")

    for country_name in countries_list:
        country_code = pycountry.countries.lookup(country_name).alpha_3
        country = Country(iso=country_code, name=country_name)
        session.add(country)
        session.commit()

    session.close()


def insert_asset_classes(df: pd.DataFrame):
    session = Database.get_session()
    assets_classes_list = column_to_unique_list(df, "commitment_asset_class")

    for asset_class_name in assets_classes_list:
        asset_class_code = asset_class_name.upper().replace(" ", "_")
        asset_class = AssetClass(asset_class_code=asset_class_code, asset_class=asset_class_name)
        session.add(asset_class)
        session.commit()

    session.close()


def insert_investors(df: pd.DataFrame):
    session = Database.get_session()

    investors_list = column_to_unique_list(df, "investor_name")

    for investor_name in investors_list:
        # get the investory type from the dataframe
        investory_type_name = df[df["investor_name"] == investor_name]["investory_type"].iloc[0]

        # look up the investory type code
        investory_type_code = session.query(InvestoryType).filter_by(investory_type=investory_type_name).first().investory_type_code
        if investory_type_code is None:
            raise LookupError("Investor type not found")

        # look up the investor code
        investor_code = lookup_investor_code_by(investor_name)

        # other investor values
        created_string = df[df["investor_name"] == investor_name]["investor_date_added"].iloc[0]
        last_updated_string = df[df["investor_name"] == investor_name]["investor_last_updated"].iloc[0]
        created_epoch = date_string_to_epoch(created_string)
        last_updated_epoch = date_string_to_epoch(last_updated_string)

        country = df[df["investor_name"] == investor_name]["investor_country"].iloc[0]
        country_iso = session.query(Country).filter_by(name=country).first().iso

        # create the investor
        investor = Investor(
            investor_code=investor_code,
            name=investor_name,
            created_epoc=created_epoch,
            last_updated_epoc=last_updated_epoch,
            country_iso=country_iso,
            investory_type_code=investory_type_code,
        )

        session.add(investor)
        session.commit()

    session.close()


def insert_commitments(df: pd.DataFrame):
    session = Database.get_session()

    # loop the dataframe
    for index, row in df.iterrows():
        investor_name = row["investor_name"]
        investor_code = lookup_investor_code_by(investor_name)
        asset_class_code = row["commitment_asset_class"].upper().replace(" ", "_")
        currency_code = row["commitment_currency"]
        amount = row["commitment_amount"]

        commitment = Commitment(investor_code=investor_code, asset_class_code=asset_class_code, currency_code=currency_code, amount=amount)

        session.add(commitment)

    session.commit()  # larger number of objects, let's commit after the loop
    session.close()


def lookup_investor_code_by(name: str) -> str:
    # determine base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # read our csv into a pandas dataframe and find rows that match the investor name
    investor_codes_csv_path = os.path.join(base_dir, "creation", "investor_codes.csv")
    df = pd.read_csv(investor_codes_csv_path)
    matching_rows = df[df["investor_name"] == name]

    if not matching_rows.empty:
        investor_code = matching_rows["investor_code"].iloc[0]
        return investor_code if not pd.isnull(investor_code) else "---"
    else:
        return "---"


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
