from http import HTTPStatus


def test_create_payment(client, payment_form):
    payment_form["date"] = "2020-01-01"
    response = client.post("/payments", json=payment_form)
    assert response.status_code == HTTPStatus.CREATED
    expected = [
        {
            "amount": 500,
            "category": "Salud",
            "date": "2020-01-01",
            "description": "description",
            "installment": 1,
            "installments": 4,
            "method": "credito",
            "password": "**********",
            "username": "user",
        },
        {
            "amount": 500,
            "category": "Salud",
            "date": "2020-02-10",
            "description": "description",
            "installment": 2,
            "installments": 4,
            "method": "credito",
            "password": "**********",
            "username": "user",
        },
        {
            "amount": 500,
            "category": "Salud",
            "date": "2020-03-10",
            "description": "description",
            "installment": 3,
            "installments": 4,
            "method": "credito",
            "password": "**********",
            "username": "user",
        },
        {
            "amount": 500,
            "category": "Salud",
            "date": "2020-04-10",
            "description": "description",
            "installment": 4,
            "installments": 4,
            "method": "credito",
            "password": "**********",
            "username": "user",
        },
    ]
    assert response.json() == expected
