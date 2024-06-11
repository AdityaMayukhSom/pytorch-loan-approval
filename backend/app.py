from fastapi import FastAPI


application = FastAPI()


@application.get("/hello")
def hello_route():
    return {"Hello": "ABC"}
