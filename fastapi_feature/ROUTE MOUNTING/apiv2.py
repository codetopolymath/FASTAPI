from fastapi import FastAPI


apiv2 = FastAPI()

@apiv2.get('/location')
def index():
    return {"Location": "India"}
