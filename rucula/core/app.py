from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from rucula.payments.router import router as payments


def create_app():
    """ """
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    app.include_router(payments)
    app.mount("/", StaticFiles(directory="rucula/static", html=True), name="static")

    return app
