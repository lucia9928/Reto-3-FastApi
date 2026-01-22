from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()
app.title= "mi primera aplicacion con fastapi"
app.version="2.0.0"

movies=[{
    "id":1,
    "title":"El señor de los anillos",
    "category": "fantasia",
    "año":2025}]

@app.get("/", tags =['home'])
def home():
    return {"Hello": "World"}


@app.get('/movies',tags=['Movies'])
def home():
    return movies


@app.get('/movies/{id}',tags=['Movies'])
def get_movie(id:int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return []


@app.get('/movies/',tags=['Movies'])
def get_movie_by_category(category:str, year:int):
    for movie in movies:
        if movie['category'] == category:
            return movie
    return []

@app.post('/movies/',tags=['Movies'])
def create_movie(id:int=Body(), title:str=Body(), category:str=Body(), year:int=Body()):
    movies.append({
        "id":id,
        "title":title,
        "category":category,
        "year":year
    })
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movies(id:int, title:str=Body(), category:str=Body(), year:int=Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['category'] = category
            movie['year'] = year
        return movie
    return movies
@app.delete('/movies/{id}', tags=['Movies'])
def update_movies(id:int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)

    return movies


