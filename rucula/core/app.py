from fastapi import FastAPI
from fastapi.param_functions import Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from rucula.core.auth import authenticate
from rucula.core.models import Payment
from rucula.core.service import PaymentService


def create_app():
    """ """
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="rucula/static/public"), name="static")

    templates = Jinja2Templates(directory="rucula/static/templates")

    @app.get("/", response_class=HTMLResponse)
    def get_form(request: Request):
        """ """
        context = {"request": request}
        return templates.TemplateResponse("form.html", context=context)

    @app.post("/payments", response_class=HTMLResponse)
    async def create_payment(request: Request, payment: Payment = Depends()):
        """ """
        authenticate(payment.username, payment.password)
        PaymentService.save(payment)
        context = {"request": request}
        return templates.TemplateResponse("result.html", context=context)

    return app
