from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    # Acceder a una variable de entorno
    api_key = os.getenv("SUPABASE_URL")
    return {"Hello": "World", "API_KEY": api_key}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}