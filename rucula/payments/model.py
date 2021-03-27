from pydantic import BaseModel
from pydantic import SecretStr


class Payment(BaseModel):

    username: str
    password: SecretStr
    category: str
    description: str
    method: str
    amount: int
    installments: int
