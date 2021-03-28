from rucula.core.logging import logger
from rucula.payments.google import PaymentForm
from rucula.payments.model import Payment


class PaymentService:
    @staticmethod
    def save(payment: Payment):
        """ """
        PaymentForm.save(payment)
        logger.info(f"Saved payment {payment=}")
