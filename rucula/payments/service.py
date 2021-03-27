from rucula.core.logging import logger
from rucula.payments.model import Payment


class PaymentService:
    @staticmethod
    def save(payment: Payment):
        """ """
        logger.info(f"Saving payment {payment}")
