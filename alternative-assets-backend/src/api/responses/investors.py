from typing import List

from pydantic import BaseModel


class InvestorResponse(BaseModel):
    investor_code: str
    name: str
    country_iso: str
    country_name: str
    investory_type_code: str
    investory_type: str
    total_commitment: int
    created_epoch: int

    model_config = {
        "from_attributes": True
    }
