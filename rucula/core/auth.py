from fastapi import Query

from rucula.core.config import settings
from rucula.core.exceptions import UnauthorizedRequest


def verify_session(token=Query(default="")):
    """ """
    if token != settings.TOKEN:
        raise UnauthorizedRequest()
    return token
