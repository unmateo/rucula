from http import HTTPStatus

from pytest import raises

from rucula.core.exceptions import ServiceUnavailable
from rucula.payments.google import PaymentForm


def test_save_response_success(payment):
    response = PaymentForm.save(payment)
    assert response.status_code == HTTPStatus.OK


def test_save_response_failure(payment):
    with raises(ServiceUnavailable):
        payment.category = ""
        PaymentForm.save(payment)
