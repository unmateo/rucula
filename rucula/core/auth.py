from pydantic import SecretStr

from rucula.core.config import settings
from rucula.core.exceptions import UnauthorizedRequest


def authenticate(username: str, password: SecretStr):
    """ """
    user_ok = username == settings.USERNAME
    pass_ok = password.get_secret_value() == settings.PASSWORD
    if not (user_ok and pass_ok):
        raise UnauthorizedRequest()
