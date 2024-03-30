from fastapi import FastAPI
from db.peticionesfilms import get_films, get_filmbyId, add_film, update_film, delete_film
from Model.Film import Film

app = FastAPI()

@app.get("/films/")
async def read_films():
    try:
        return await get_films()
    except Exception as e:
        return {"status": -1, "message": str(e)}

@app.get("/films/{id}")
async def read_film(id: str):
    try:
        return await get_filmbyId(id)
    except Exception as e:
        return {"status": -1, "message": str(e)}

@app.post("/films/")
async def create_film(film: Film):
    try:
        return await add_film(film)
    except Exception as e:
        return {"status": -1, "message": str(e)}
    
@app.put("/films/{id}")
async def update_film_data(id: str, film: Film):
    try:
        return await update_film(id, film)
    except Exception as e:
        return {"status": -1, "message": str(e)}
    
@app.delete("/films/{id}")
async def delete_film_data(id: str):
    try:
        return await delete_film(id)
    except Exception as e:
        return {"status": -1, "message": str(e)}    