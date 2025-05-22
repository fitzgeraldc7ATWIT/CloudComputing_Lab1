import time
import datetime

from fastapi import FastAPI
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


# @app.get("/car")
# async def car():
#     return {"message": "Hello World"}
#
#
# @app.get("/sports")
# async def sports():
#     return {"message": "Hello World"}
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}