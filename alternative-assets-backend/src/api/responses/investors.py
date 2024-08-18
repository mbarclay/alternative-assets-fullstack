from pydantic import BaseModel


class InvestorResponse(BaseModel):
    investor_code: str
    name: str
    country_iso: str
    country_name: str
    investory_type_code: str
    investory_type: str
    total_commitment: int
    added_epoch: int

    model_config = {"from_attributes": True}


class AssetsByInvestorSummaryResponse(BaseModel):
    asset_class_code: str
    asset_class: str
    total_commitment_amount: int

    model_config = {"from_attributes": True}


class InvestorCommitmentsResponse(BaseModel):
    commitment_uuid: str
    asset_class_code: str
    asset_class: str
    currency_code: str
    amount: int

    model_config = {"from_attributes": True}
