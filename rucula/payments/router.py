from http import HTTPStatus

from fastapi import APIRouter

from rucula.core.auth import authenticate
from rucula.payments.model import Payment
from rucula.payments.service import PaymentService


router = APIRouter(prefix="/payments")


@router.post("", status_code=HTTPStatus.CREATED, response_model=Payment)
def create_payment(payment: Payment):
    """ """
    authenticate(payment.username, payment.password)
    PaymentService.save(payment)
    return payment
