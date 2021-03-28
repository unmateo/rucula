from pytest import fixture

from rucula.payments.model import Payment


@fixture
def payment_form():
    """ """
    form = {
        "username": "user",
        "password": "pass",
        "category": "Salud",
        "description": "description",
        "method": "method",
        "amount": 100,
        "installments": 6,
    }

    return form


@fixture
def payment(payment_form):
    """ """
    return Payment(**payment_form)
