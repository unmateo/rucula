from fastapi.testclient import TestClient
from pytest import fixture

from rucula.core.app import create_app


@fixture
def app():
    return create_app()


@fixture
def client(app):
    return TestClient(app)
