#from fastapi import FastAPI, Cookie
#from pydantic import BaseModel

#app = FastAPI()

#@app.get("/readcookie")
#async def read_cookie(username: str = Cookie(None)):
#    return {"username": username}

#@app.get("/getHeader")
#async def

import time
import datetime
from urllib.request import Request

from fastapi import FastAPI, Cookie, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root_route():
    return {"message": "Hello World"}

@app.get("/time")
async def time():
    return {"time" : datetime.datetime.now().time()}

@app.get("/animal/{name}")
async def animal(name: str):
    return {"Your favorite animal": name}


@app.get("/color/{name}")
async def color(name: str):
    return {"Your favorite color": name}

class CollegeStudentInput(BaseModel):
    name: str
    age: int
    year: int
    major: str

@app.post("/college-student")
async def college_student(input: CollegeStudentInput):
    return (f"Hello {input.name}, you are {input.age} years old,"
            f"and a {input.major} major in your {input.year} year.")


@app.get("/query")
async def query(name: str, age: int, country: str):
    return f"Hello {name}, you are {age} years old, and live in {country}."


class CarMakeModel(BaseModel):
    make: str
    model: str
    year: int

@app.post("/car")
async def car(input: CarMakeModel):
    return f"You have a {input.make} {input.model} from {input.year}."


@app.get("/sports")
async def sports(name: str):
    return f"Your favorite sport is {name}."


@app.get("/book")
async def root(genre: str, book: str):
    return f"Your favourite genre is {genre}, and favourite book in that genre is {book}."


@app.get("/hometown")
async def root(highschool: str, town: str):
    return f"You went to {highschool} in {town}."

@app.get("/read_cookie")
async def read_cookie(username: str = Cookie(None)):
    return {"username": username}

@app.get("/headers/")
async def get_headers(request: Request):
    user_agent = request.headers.get("user-agent")
    x_custom = request.headers.get("x-custom-header")
    user_email = request.headers.get("user_email")
    my_val = request.headers.get("my-val")

    return {
        "User-Agent": user_agent,
        "X-Custom-Header": x_custom,
        "user_email": user_email,
        "my-val": my_val
    }