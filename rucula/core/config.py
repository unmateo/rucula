from functools import lru_cache

from pydantic import BaseSettings


class BaseConfig(BaseSettings):

    TOKEN: str


@lru_cache()
def load_settings(settings: BaseConfig) -> BaseConfig:
    """ """
    return settings()


settings = load_settings(BaseConfig)
