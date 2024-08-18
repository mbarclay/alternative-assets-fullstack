import uuid

from sqlalchemy import Column, ForeignKey, Index, Integer, Text
from sqlalchemy.orm import declarative_base, relationship

# import path for declarative_base
Base = declarative_base()


# define the asset class model
class AssetClass(Base):
    __tablename__ = "asset_classes"

    asset_class_code = Column(Text, primary_key=True, nullable=False)
    asset_class = Column(Text, nullable=False)


# define the country model
class Country(Base):
    __tablename__ = "countries"

    iso = Column(Text(3), primary_key=True, nullable=False)
    name = Column(Text)


# define the investory type model
class InvestoryType(Base):
    __tablename__ = "investory_types"

    investory_type_code = Column(Text, primary_key=True, nullable=False)
    investory_type = Column(Text, nullable=False)


# define the investor model
class Investor(Base):
    __tablename__ = "investors"

    investor_code = Column(Text, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    added_epoch = Column(Integer, nullable=False)
    last_updated_epoch = Column(Integer, nullable=False)
    country_iso = Column(Text(3), ForeignKey("countries.iso"), nullable=False)
    investory_type_code = Column(Text, ForeignKey("investory_types.investory_type_code"), nullable=False)

    # relationships
    country = relationship("Country", back_populates="investors")
    investory_type = relationship("InvestoryType", back_populates="investors")
    commitments = relationship("Commitment", back_populates="investor")


Country.investors = relationship("Investor", order_by=Investor.investor_code, back_populates="country")
InvestoryType.investors = relationship("Investor", order_by=Investor.investor_code, back_populates="investory_type")


# define the commitment model
class Commitment(Base):
    __tablename__ = "commitments"

    commitment_uuid = Column(Text, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    investor_code = Column(Text, ForeignKey("investors.investor_code"), nullable=False)
    asset_class_code = Column(Text, ForeignKey("asset_classes.asset_class_code"), nullable=False)
    currency_code = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)

    # relationships
    investor = relationship("Investor", back_populates="commitments")
    asset_class = relationship("AssetClass")


# define indexes
Index("commitments_asset_class_code_index", Commitment.asset_class_code)
Index("commitments_currency_code_index", Commitment.currency_code)
Index("commitments_investor_code_index", Commitment.investor_code)
