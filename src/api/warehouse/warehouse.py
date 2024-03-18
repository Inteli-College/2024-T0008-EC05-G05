# O objetivo desse código é funcionar como a api da tela de estoque do sistema. 
# A ideia é que a tela de supplies faça requisições para essa api para obter informações sobre os produtos e para adicionar novos produtos ao estoque. 


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tinydb import TinyDB, Query
from typing import List
import json
import os
from datetime import datetime






# Modelo de dados para realizar o post no DB 
class Post(BaseModel):
    nome_kit: str
    id_kit: int
    item_1: List[str] 




# Inicia o servidor FastAPI
app = FastAPI()

# Inicia o banco de dados com tinyDb
db = TinyDB('kits.json')
posts_table = db.table('kits')

# Liberando o CORS para fazer requisições locais
app.add_middleware(
    CORSMiddleware,
    # Definindo as origens que podem fazer requisições
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Função para criar uma entrada no arquivo de logs 

def log_update_time(post_id: int):
 
    windows_username = os.getenv('USERNAME')

    # Padrão da entrada no log
    log_entry = {"kit_id": post_id, "hora da atualização": datetime.now().isoformat(), "nome user windows": windows_username}

    with open("logs.json", "a", encoding="utf-8") as log_file:
        json.dump(log_entry, log_file, ensure_ascii=False)
        log_file.write("\n")



@app.get("/")
def hello():
    return {"Hello World"}

# Endpoint para criar um novo kit
@app.post("/posts/")
def create_post(post: Post):
    post_dict = post.dict()
    post_id = posts_table.insert(post_dict)
    return {"post_id": post_id, **post_dict}

# Endpoint para fazer um get em id único 
@app.get("/posts/{post_id}")
def read_post(post_id: int):
    post = posts_table.get(doc_id=post_id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Endpoint de todos os kits
@app.get("/posts/")
def read_all_posts():
    return posts_table.all()

# Endpoint de update de um kit 
@app.put("/posts/{post_id}")
def update_post(post_id: int, post_data: Post):
    post_dict = post_data.dict()
    existing_post = posts_table.get(doc_id=post_id)
    if existing_post:
        posts_table.update(post_dict, doc_ids=[post_id])
        log_update_time(post_id)

        return {"message": "Kit atualizado", "kit_id": post_id, **post_dict}
    else:
        raise HTTPException(status_code=404, detail="kit não encontrado")


# Para rodar o código, basta rodar o comando "uvicorn warehouse:app --reload" no terminal.