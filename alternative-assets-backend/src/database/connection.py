import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import settings


class Database:
    @staticmethod
    def get_session():
        """
        create a database connection.
        """
        # determine base directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # define the relative path to the database
        db_path = os.path.join(base_dir, "database", f"{settings.database_name}.sqlite")

        # create the sqlite engine with the relative path
        engine = create_engine(f"sqlite:///{db_path}")

        # create a session
        with Session(bind=engine) as session:
            return session
