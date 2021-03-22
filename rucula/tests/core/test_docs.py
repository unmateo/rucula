def test_docs(client):
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc(client):
    response = client.get("/redoc")
    assert response.status_code == 200
