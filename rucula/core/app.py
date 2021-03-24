from fastapi import Depends
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from rucula.core.auth import verify_session
from rucula.core.exceptions import UnauthorizedRequest


def create_app():
    """ """
    app = FastAPI(dependencies=[Depends(verify_session)])

    app.mount("/static", StaticFiles(directory="rucula/static/public"), name="static")

    templates = Jinja2Templates(directory="rucula/static/templates")

    @app.exception_handler(UnauthorizedRequest)
    async def unauthorized_exception_handler(
        request: Request, exc: UnauthorizedRequest
    ):
        """ """
        context = {"request": request}
        return templates.TemplateResponse("public.html", context=context)

    @app.get("/", response_class=HTMLResponse)
    def frontend(request: Request):
        """ """
        context = {"request": request}
        return templates.TemplateResponse("form.html", context=context)

    return app
