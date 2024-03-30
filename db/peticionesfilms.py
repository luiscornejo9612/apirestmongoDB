from datetime import datetime
from fastapi import HTTPException
from db.dbconnection import collection
from Model.Film import Film
from bson import ObjectId

def convert_objectid_to_str(obj):
    if isinstance(obj, dict):
        return {k: str(v) if isinstance(v, ObjectId) else v for k, v in obj.items()}
    elif isinstance(obj, list):
        return [str(item) if isinstance(item, ObjectId) else item for item in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)
    return obj

# Obtener todos los films
async def get_films():
    films = collection.find({})
    films = [convert_objectid_to_str(film) for film in films]
    films = [convert_objectid_to_str(film) for film in films]
    return {"status": 1, "data": films}

# Obtener un film por su ID
async def get_filmbyId(id: str):
    film = collection.find_one({"_id": ObjectId(id)})
    if film:
        film = convert_objectid_to_str(film)
        return {"status": 1, "data": film}
    else:
        raise HTTPException(status_code=404, detail="Film no encontrada")

# Añadir un nuevo film
async def add_film(film: Film):
    film.created_at = datetime.now()
    film.update_at = datetime.now()
    result = collection.insert_one(film.dict())
    return {"status": 1, "data": {"id": str(result.inserted_id)}}

# Actualizar un film existente
async def update_film(id: str, film: Film):
    film.update_at = datetime.now()
    film.update_at = datetime.now()
    result = collection.replace_one({"_id": ObjectId(id)}, film.dict())
    if result.modified_count == 1:
        return {"status": 1, "message": "Film ha sido actualizada"}
    else:
        raise HTTPException(status_code=404, detail="Film no encontrada")

# Eliminar un film por su ID
async def delete_film(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"status": 1, "message": "Film ha sido eliminada"}
    else:
        raise HTTPException(status_code=404, detail="Film no encontrada")

