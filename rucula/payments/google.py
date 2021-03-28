from http import HTTPStatus

from requests import post

from rucula.core.config import settings
from rucula.core.exceptions import ServiceUnavailable
from rucula.core.logging import logger
from rucula.payments.model import Payment


class PaymentForm:

    base_url = "https://docs.google.com/forms/u/0/d/e/{form_id}/formResponse"

    @classmethod
    def save(cls, payment: Payment):
        """ """
        config = settings.FORM
        endpoint = cls.base_url.format(form_id=config.FORM_ID)
        form = {
            f"entry.{config.FORM_FIELD_SECRET}": config.FORM_SECRET.get_secret_value(),
            f"entry.{config.FORM_FIELD_DESCRIPTION}": payment.description,
            f"entry.{config.FORM_FIELD_AMOUNT}": payment.amount,
            f"entry.{config.FORM_FIELD_CATEGORY}": payment.category,
        }
        response = post(endpoint, data=form)
        if response.status_code != HTTPStatus.OK:
            logger.error(f"Couldn't save {payment=} using config {config=}")
            raise ServiceUnavailable()
        return response
