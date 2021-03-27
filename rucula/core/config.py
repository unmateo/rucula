from functools import lru_cache

from pydantic import BaseSettings


class BaseConfig(BaseSettings):

    USERNAME: str
    PASSWORD: str

    LOG_LEVEL: str = "INFO"


@lru_cache()
def load_settings(settings: BaseConfig) -> BaseConfig:
    """ """
    return settings()


settings = load_settings(BaseConfig)
