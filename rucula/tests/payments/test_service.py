from datetime import date as Date

from rucula.core.config import settings
from rucula.payments.service import PaymentService


INSTALLMENT_DAY = settings.INSTALLMENT_DAY


def test_installment_dates_0_installments(payment):
    """ Should return payment date. """
    payment.installments = 0
    dates = PaymentService.installment_dates(payment=payment)
    assert dates == [payment.date]


def test_installment_dates_1_installment(payment):
    """ Should return payment date. """
    payment.installments = 1
    dates = PaymentService.installment_dates(payment=payment)
    assert dates == [payment.date]


def test_installment_dates_2_installments(payment):
    """ Should return payment date and next month's date. """
    payment.installments = 2
    payment.date = Date(year=2020, month=1, day=1)
    dates = PaymentService.installment_dates(payment=payment)
    expected = [payment.date, Date(year=2020, month=2, day=INSTALLMENT_DAY)]
    assert dates == expected


def test_installment_dates_3_installments(payment):
    """ Should return payment date and two following months dates. """
    payment.installments = 3
    payment.date = Date(year=2020, month=12, day=30)
    dates = PaymentService.installment_dates(payment=payment)
    expected = [
        payment.date,
        Date(year=2021, month=1, day=INSTALLMENT_DAY),
        Date(year=2021, month=2, day=INSTALLMENT_DAY),
    ]
    assert dates == expected
