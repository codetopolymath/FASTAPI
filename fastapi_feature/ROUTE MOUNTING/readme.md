Mount different FastAPI apps for different routes:
Following the same rules of mounting different WSGI applications for different routes, you can also mount different FastAPI applications within the FastAPI application. This would mean that every sub-FastAPI application would have its docs, would run independent of other applications, and will handle its path-specific requests. To mount this, simply create a master application and sub-application file. Now, import the app object from the sub-application file to the master application file and pass this object directly to the mount function of the master application object. This workaround doesn’t require any middleware. See an example below:

Below are the contents for the apiv1.py file (sub-application 1):[Code for sub-application 1]

from fastapi import FastAPI


apiv1 = FastAPI()

@apiv1.get('/name')
def index():
    return {"Name": "Rohit Ghawale"}



And here is the code for the apiv2.py file (sub-application 2): [Code for sub-application 2]

from fastapi import FastAPI


apiv2 = FastAPI()

@apiv2.get('/location')
def index():
    return {"Location": "India"}


Now, we can mount both of these sub-applications in the master application. See the code for the master.py file: [code for The master application code where both sub-applications are mounted]

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



If you make requests to respective paths endpoints, the request will be handled by those sub-applications.


Here both the requests were served by respective applications at endpoint as 127.0.0.1:8001/api/v1/name , 127.0.0.1:8001/api/v2/location
 
