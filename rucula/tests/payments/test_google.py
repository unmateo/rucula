from http import HTTPStatus

from httpx import AsyncClient
from pytest import mark
from pytest import raises

from rucula.core.exceptions import ServiceUnavailable
from rucula.payments.google import PaymentForm


async def test_save_one_response_success(payment):
    async with AsyncClient() as client:
        response = await PaymentForm.save_one(payment=payment, client=client)
        assert response.status_code == HTTPStatus.OK


async def test_save_one_response_failure(payment):
    with raises(ServiceUnavailable):
        payment.category = ""
        async with AsyncClient() as client:
            await PaymentForm.save_one(payment=payment, client=client)


@mark.async_timeout(1)
async def test_save_many_response_success(payment):
    payments = [payment, payment]
    responses = await PaymentForm.save_many(payments=payments)
    assert len(responses) == len(payments)
    for response in responses:
        assert response.status_code == HTTPStatus.OK
