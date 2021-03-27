from http import HTTPStatus


def test_openapi(client):
    response = client.get("/openapi.json")
    assert response.status_code == HTTPStatus.NOT_FOUND
