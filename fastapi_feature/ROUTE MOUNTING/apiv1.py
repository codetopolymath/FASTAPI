from fastapi import FastAPI


apiv1 = FastAPI()

@apiv1.get('/name')
def index():
    return {"Name": "Rohit Ghawale"}
