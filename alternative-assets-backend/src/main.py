import time

from src.database.connection import Database
from src.model.assets_under_management import AssetClass, Commitment, Country, Investor, InvestoryType


def insert_sample_data():
    # get our database session
    session = Database.get_session()

    # Create a new asset class
    asset_class = AssetClass(asset_class_code="EQ", asset_class="Equity")
    session.add(asset_class)

    # Create a new country
    country = Country(iso="USA", name="United States")
    session.add(country)

    # Create a new investory type
    investory_type = InvestoryType(investory_type_code="INST", investory_type="Institutional")
    session.add(investory_type)

    # Create a new investor
    investor = Investor(
        investor_code="INV_001", name="Investor A", created_epoc=int(time.time()), last_updated_epoc=int(time.time()), country_iso="USA", investory_type_code="INST"
    )
    session.add(investor)

    # Create a new commitment
    commitment = Commitment(investor_code="INV_001", asset_class_code="EQ", currency_code="USD", amount=1000000)
    session.add(commitment)

    # commit and close
    session.commit()
    session.close()


if __name__ == "__main__":
    insert_sample_data()
