def test_index(client):
    response = client.get("/")
    with open("rucula/index.html") as index:
        expected = index.read()
    assert response.text == expected
