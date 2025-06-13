# Creating First Endpoint & Running and Exploring Docs

"""
pip install fastapi uvicorn
--> fastapi: the framework itself
--> uvicorn: a lightning‑fast ASGI(Asynchronous Server Gateway Interface) server to run your app

"""
# 1. Import Library
from fastapi import FastAPI

# 2. Instantiate the FastAPI "app"
app = FastAPI()

# 3. Define an endpoint with some method(GET/POST/...)

# lets Define a GET endpoint at the root path
@app.get("/")
def get_root():
    return {"message": "I had created my first End-Point"}

# The @app.get("/") decorator tells FastAPI: “When someone does an HTTP GET on /, run read_root()


"""
Run the server

CMD-->  uvicorn module_1:app --reload

to see output: Endpoint:         http://127.0.0.1:8000/
Interactive docs (Swagger UI):   http://127.0.0.1:8000/docs    #Automatic Documentation.
Alternative docs (ReDoc):        http://127.0.0.1:8000/redoc

"""

# Lets me create other route

@app.get("/about")
def ab():
    return {"This is the about section"}

# http://127.0.0.1:8000/about


# New route using path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"Greetings": f"Hello, {name}. Nice to meet you"}

# http://127.0.0.1:8000/hello/jinil --> o/p=  {"Greetings":"Hello, jinil. Nice to meet you"}


