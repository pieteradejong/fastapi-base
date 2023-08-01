from datetime import date
from pydantic import BaseModel, Field, validator

"""
Not actual app logic - just an example of what a model might look like.
"""

class User(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100, description="User first name.")
    last_name: str = Field(..., min_length=1, max_length=100, description="User last name.")
    date_of_birth: date = Field(...)
    height: float = Field(..., gt=0)
    address: str = Field(..., min_length=1, max_length=500)

@validator("date_of_birth")
def validate_date_of_birth(cls, dob):
    if dob > date.today():
        raise ValueError("Date of birth cannot be in the future")
    return dob
