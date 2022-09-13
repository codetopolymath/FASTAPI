
from fastapi import FastAPI
from apiv1 import apiv1
from apiv2 import apiv2
import uvicorn

app = FastAPI()
app.mount("/api/v1", apiv1)
app.mount("/api/v2", apiv2)


@app.get('/')
def index():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run("master:app", host='127.0.0.1', port=8000, reload=True)
