import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import settings


class Database:
    _engine = None
    _SessionFactory = None

    @staticmethod
    def _initialize_engine():
        """Initialize the SQLAlchemy engine and session factory."""
        if Database._engine is None:
            # determine base directory
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # define the path to the database
            db_path = os.path.join(base_dir, "database", f"{settings.database_name}.sqlite")

            # create the sqlite engine with the relative path
            Database._engine = create_engine(f"sqlite:///{db_path}", echo=True)
            Database._SessionFactory = sessionmaker(bind=Database._engine)

    @staticmethod
    def get_session() -> Session:
        """
        Get a new session instance. The caller is responsible for closing the session.
        """
        if Database._SessionFactory is None:
            Database._initialize_engine()

        return Database._SessionFactory()

    @staticmethod
    def session_scope():
        """
        Provide a transactional scope around a series of operations.
        This is a context manager that automatically commits or rolls back a transaction.
        """
        session = Database.get_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
