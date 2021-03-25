from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def create_app():
    """ """
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="rucula/static/public"), name="static")

    templates = Jinja2Templates(directory="rucula/static/templates")

    @app.get("/", response_class=HTMLResponse)
    def get(request: Request):
        """ """
        context = {"request": request}
        return templates.TemplateResponse("form.html", context=context)

    @app.post("/", response_class=HTMLResponse)
    async def post(request: Request):
        """ """
        form = await request.form()
        print(form)
        context = {"request": request}
        return templates.TemplateResponse("result.html", context=context)

    return app
