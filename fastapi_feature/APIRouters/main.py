
from fastapi import FastAPI
from book import bookroute
from novel import novelroute
import uvicorn

app = FastAPI()
app.include_router(bookroute, prefix="/book")
app.include_router(novelroute, prefix="/novel")


@app.get('/')
def index():
    return "this is illustration of APIRouter"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
