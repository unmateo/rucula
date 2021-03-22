def test_openapi(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
