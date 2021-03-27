from http import HTTPStatus


def test_create_payment(client, payment_form):
    response = client.post("/payments", json=payment_form)
    assert response.status_code == HTTPStatus.CREATED
