from http import HTTPStatus
from typing import List

from httpx import AsyncClient

from rucula.core.config import settings
from rucula.core.exceptions import ServiceUnavailable
from rucula.core.logging import logger
from rucula.payments.model import Payment


class PaymentForm:

    base_url = "https://docs.google.com/forms/u/0/d/e/{form_id}/formResponse"

    @classmethod
    async def save_one(cls, payment: Payment, client: AsyncClient):
        """ """
        config = settings.FORM
        endpoint = cls.base_url.format(form_id=config.FORM_ID)
        form = {
            f"entry.{config.FORM_FIELD_SECRET}": config.FORM_SECRET.get_secret_value(),
            f"entry.{config.FORM_FIELD_DESCRIPTION}": payment.description,
            f"entry.{config.FORM_FIELD_AMOUNT}": payment.amount,
            f"entry.{config.FORM_FIELD_CATEGORY}": payment.category,
            f"entry.{config.FORM_FIELD_DATE}_year": payment.date.year,
            f"entry.{config.FORM_FIELD_DATE}_month": payment.date.month,
            f"entry.{config.FORM_FIELD_DATE}_day": payment.date.day,
            f"entry.{config.FORM_FIELD_METHOD}": payment.method,
            f"entry.{config.FORM_FIELD_INSTALLMENT}": payment.installment,
            f"entry.{config.FORM_FIELD_INSTALLMENTS}": payment.installments,
        }
        response = await client.post(endpoint, data=form)
        if response.status_code != HTTPStatus.OK:
            logger.error(f"Couldn't save {payment=} using config {config=}")
            raise ServiceUnavailable()
        else:
            logger.info(f"Saved {payment=}")
        return response

    @classmethod
    async def save_many(cls, payments: List[Payment]):
        """ """
        responses = []
        async with AsyncClient() as client:
            for payment in payments:
                response = await cls.save_one(payment=payment, client=client)
                responses.append(response)
            logger.info(f"Finished saving {len(payments)} payments.")
        return responses
