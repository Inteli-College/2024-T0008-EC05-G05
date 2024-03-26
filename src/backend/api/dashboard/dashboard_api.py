from fastapi import FastAPI
from tinydb import TinyDB, Query
from typing import List
from pydantic import BaseModel

app = FastAPI()
db = TinyDB('db.json')

class Item(BaseModel):
    id: int
    nome: str

class Kit(BaseModel):
    id: int
    numero_do_kit: int
    itens: List[int]

@app.get("/api/itens", response_model=List[Item])
async def get_itens():
    itens_table = db.table('itens')
    itens = itens_table.all()
    return itens

@app.get("/api/kits", response_model=List[Kit])
async def get_kits():
    kits_table = db.table('kits')
    kits = kits_table.all()
    return kits
