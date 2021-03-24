from fastapi import HTTPException


class UnauthorizedRequest(HTTPException):
    def __init__(self):
        super().__init__(401, "not authenticated")
