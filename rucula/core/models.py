from typing import Optional

from fastapi import Form
from pydantic import BaseModel
from pydantic import SecretStr


def as_form(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


@as_form
class Payment(BaseModel):

    username: str
    password: SecretStr
    category: str
    description: str
    method: str
    amount: int
    installments: int
