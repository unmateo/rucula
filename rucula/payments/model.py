from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import SecretStr
from pydantic import validator


class Payment(BaseModel):

    username: str
    password: SecretStr
    category: str
    description: str
    method: str
    amount: int
    installments: int
    date: Optional[date]

    @validator("date", pre=True, always=True)
    def set_date(cls, v):
        return v or date.today()
