
from fastapi import APIRouter


novelroute = APIRouter()

@novelroute.get('/info')
def novels():
    return {"detail": "This novel info is from the novel APIRouter",
    "name": "I am good",
    "publication": "Rohit"}
