from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class FormData(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    country: str = Field(..., min_length=2, max_length=50)
    phone_number: str = Field(..., min_length=10, max_length=15)
    languages_frameworks: List[str] = Field(..., min_items=1)
    coding_experience: str = Field(..., min_length=1, max_length=50)
    annual_compensation: Optional[float] = None
    certifying_statement: bool
    linkedin_url: Optional[str] = None