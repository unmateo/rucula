from pytest import fixture

from rucula.payments.model import Payment


@fixture
def payment_form():
    """ """
    form = {
        "username": "user",
        "password": "pass",
        "category": "Salud",
        "description": "jaja",
        "method": "jaja",
        "amount": 100,
        "installments": 1,
    }

    return form


@fixture
def payment(payment_form):
    """ """
    return Payment(**payment_form)
