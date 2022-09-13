
It usually happens that as your application grows bigger, it becomes a mess to manage all the routes in one place. Sometimes, overlaps can happen or you might be duplicating a route unaware of the consequences later. What if there was a system where you could group your routes into different file structures and easily manage them?

FastAPI has a system of APIRouters. These can be considered to be mini FastAPI apps that are part of the bigger application. This means that one can break bigger application routes into small units of APIRouters and mount individual APIRouters in the main application.

Do note here that these APIRouters are part of the bigger application and not the independent applications like the ones we saw in the above two sections. Therefore, all the routes from all the APIRouters will be listed in the main application documentation.

These APIRouters can have separate prefixes to the path operations, tags, dependencies, & responses. Therefore to implement this, you need to import the APIRouter class from fast API and then use its object to create routes as you would do in a usual FastAPI application.

Let’s see an example. Suppose we are building a library management system and we want to handle books and novel data separately. Let this be the code for the book.py file: [APIRouter usage in book.py]

from fastapi import APIRouter


bookroute = APIRouter()

@bookroute.get('/info')
def books():
    return {"detail": "This book info is from the book APIRouter",
    "name": "Hello",
    "ISBN": "32DS3"}
    
And this is the code for the novel.py file: [APIRouter usage in novel.py]

from fastapi import APIRouter


novelroute = APIRouter()

@novelroute.get('/info')
def novels():
    return {"detail": "This novel info is from the novel APIRouter",
    "name": "I am good",
    "publication": "Rohit"}


Now, to include both the routers in the main application, simply import the object of APIRouter and pass these in the include_router function of the main FastAPI application object. We will also add the prefixes for these routers so that the same endpoints in both routers don’t conflict. See the implementation below: [Code to include APIRouters in the main application]

from fastapi import FastAPI
from book import bookroute
from novel import novelroute
import uvicorn

app = FastAPI()
app.include_router(bookroute, prefix="/book")
app.include_router(novelroute, prefix="/novel")


@app.get('/')
def index():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run("demo:app", host='127.0.0.1', port=8000, reload=True)

If you hit the “/book/info” and the “/novel/info” endpoints, you will get different responses depending upon how you handled those inputs in the APIRouters.
In this way, you can have multiple APIRouters to handle parameters based on what type of operation you want to perform for those groups of endpoints.
