def test_index(client):
    response = client.get("/")
    with open("rucula/static/index.html") as index:
        expected = index.read()
    assert response.text == expected
