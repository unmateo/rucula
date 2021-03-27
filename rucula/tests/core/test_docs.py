from http import HTTPStatus


def test_docs(client):
    response = client.get("/docs")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_redoc(client):
    response = client.get("/redoc")
    assert response.status_code == HTTPStatus.NOT_FOUND
