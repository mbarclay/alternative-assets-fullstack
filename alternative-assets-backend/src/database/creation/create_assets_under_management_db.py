import os
import sqlite3

from config import settings


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


if __name__ == "__main__":
    # define the sql file path and the database name
    sql = "assets_under_management.sql"
    db = f"../{settings.database_name}.sqlite"

    # if the database already exists, delete it, we will recreate it
    if os.path.exists(db):
        os.remove(db)

    # create the database
    create_database(sql, db)
