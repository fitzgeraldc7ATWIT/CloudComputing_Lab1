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


class CarMakeModel(BaseModel):
    make: str
    model: int
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
