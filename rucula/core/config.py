from functools import lru_cache

from pydantic import BaseSettings
from pydantic import conint
from pydantic import SecretStr


class FormConfig(BaseSettings):

    FORM_ID: str
    FORM_SECRET: SecretStr

    FORM_FIELD_SECRET: str
    FORM_FIELD_CATEGORY: str
    FORM_FIELD_AMOUNT: str
    FORM_FIELD_DESCRIPTION: str
    FORM_FIELD_DATE: str
    FORM_FIELD_METHOD: str
    FORM_FIELD_INSTALLMENT: str
    FORM_FIELD_INSTALLMENTS: str


class BaseConfig(BaseSettings):

    USERNAME: str
    PASSWORD: str

    LOG_LEVEL: str = "INFO"

    FORM = FormConfig()

    INSTALLMENT_DAY: conint(ge=1, le=28) = 10


@lru_cache()
def load_settings(settings: BaseConfig) -> BaseConfig:
    """ """
    return settings()


settings = load_settings(BaseConfig)
