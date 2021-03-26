from fastapi import FastAPI
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles

from rucula.core.auth import authenticate
from rucula.core.models import Payment
from rucula.core.service import PaymentService


def create_app():
    """ """
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @app.post("/payments")
    async def create_payment(payment: Payment = Depends()):
        """ """
        authenticate(payment.username, payment.password)
        PaymentService.save(payment)
        return True

    app.mount("/", StaticFiles(directory="rucula/static", html=True), name="static")

    return app
