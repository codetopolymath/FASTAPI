from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

#staticfiles = StaticFiles(directory="~/Desktop/FASTAPI/fastapi_feature/Templates/static")
#app.mount("/static", staticfiles, name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("demo.html", {"request": request, "title": "Rohit Ghawale", "body_content": "This is the demo for using FastAPI with Jinja templates"})

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
