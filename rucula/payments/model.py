from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import SecretStr
from pydantic import validator


class Payment(BaseModel):

    amount: int
    category: str
    date: Optional[date]
    description: str
    installment: Optional[int] = 0
    installments: int
    method: str
    password: SecretStr
    username: str

    @validator("date", pre=True, always=True)
    def set_date(cls, v):
        return v or date.today()
