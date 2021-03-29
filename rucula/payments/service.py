from datetime import date as Date

from rucula.core.config import settings
from rucula.core.logging import logger
from rucula.payments.google import PaymentForm
from rucula.payments.model import Payment


class PaymentService:
    @classmethod
    async def save(cls, payment: Payment):
        """ """
        dates = cls.installment_dates(payment)
        installments = payment.installments
        amount = (
            payment.amount
            if installments < 2
            else round(payment.amount / installments, 2)
        )
        payments = [
            Payment(
                **payment.dict(exclude={"amount", "installment", "date"}),
                amount=amount,
                installment=i + 1,
                date=date,
            )
            for i, date in enumerate(dates)
        ]
        await PaymentForm.save_many(payments)
        logger.info(f"Saved payments {payments=}")
        return payments

    @classmethod
    def installment_dates(cls, payment: Payment):
        """ """
        first = payment.date
        dates = [first]
        installments = payment.installments
        if installments > 1:
            for i in range(payment.installments - 1):
                prev = dates[i]
                year, month = cls._following_month(prev)
                next_installment = Date(
                    year=year, month=month, day=settings.INSTALLMENT_DAY
                )
                dates.append(next_installment)
        return dates

    @staticmethod
    def _following_month(date: Date):
        return (date.year + 1, 1) if date.month == 12 else (date.year, date.month + 1)
