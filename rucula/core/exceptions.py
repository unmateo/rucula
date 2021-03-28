from http import HTTPStatus

from fastapi import HTTPException


class UnauthorizedRequest(HTTPException):
    def __init__(self):
        super().__init__(HTTPStatus.UNAUTHORIZED, "Not authenticated")


class ServiceUnavailable(HTTPException):
    def __init__(self):
        super().__init__(HTTPStatus.SERVICE_UNAVAILABLE, "Try later")
