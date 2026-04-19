from pydantic import BaseModel
from typing import Optional

class LeadCreate (BaseModel):
    name: str
    phone: str
    email: Optional[str]= None
    budget: str
    requirement: str
    location: str
    stage: str
    loan_required: bool
    
class LeadUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    budget: Optional[str] = None
    requirement: Optional[str] = None
    location: Optional[str] = None
    stage: Optional[str] = None
    loan_required: Optional[bool] = None