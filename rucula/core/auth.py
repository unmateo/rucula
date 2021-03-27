from pydantic import SecretStr

from rucula.core.config import settings
from rucula.core.exceptions import UnauthorizedRequest
from rucula.core.logging import logger


def authenticate(username: str, password: SecretStr):
    """ """
    user_ok = username == settings.USERNAME
    pass_ok = password.get_secret_value() == settings.PASSWORD
    auth_ok = user_ok and pass_ok
    logger.info(f"Authenticating {username=}")
    if not auth_ok:
        logger.warn(f"Failed auth for {username=}")
        raise UnauthorizedRequest()
