from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_app():
    """ """
    app = FastAPI()
    app.mount("/", StaticFiles(directory="rucula/static", html=True))
    return app
