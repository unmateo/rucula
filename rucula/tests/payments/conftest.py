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
        "method": "credito",
        "amount": 2000,
        "installments": 4,
    }

    return form


@fixture
def payment(payment_form):
    """ """
    return Payment(**payment_form)
