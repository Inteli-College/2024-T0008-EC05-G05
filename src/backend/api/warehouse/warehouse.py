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
from sqlite3 import connect
from queue import Queue
from datetime import datetime

# Modelo de dados para realizar o post no DB 
class Post(BaseModel):
    ID: int
    Item_SKUs: List[str]
    Kit_assembly_positions: str



# Inicia o servidor FastAPI
app = FastAPI()

# Liberando o CORS para fazer requisições locais
app.add_middleware(
    CORSMiddleware,
    # Definindo as origens que podem fazer requisições
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Inicia o banco de dados com SQLite
conn = connect('../../database/dbCardioBot.db')
database = conn.cursor()

# Cria um post de um novo kit dentro do DB 
@app.post("/dbsql-post/")
async def create_post(post: Post):
    # Convert the array to a string
    item_sku_str = ', '.join(post.item_sku)

    # Insert a row of data
    database.execute("INSERT INTO kits VALUES (?, ?, ?)", (post.ID, item_sku_str, post.assembly_position))

    # Save (commit) the changes
    conn.commit()

    return {"message": "Post has been created successfully."}

@app.get("/")
def hello():
    return {"Hello World"}


# Endpoint de todos os kits
@app.get("/posts/")
def read_all_posts():
     # Establish a new connection
    conn = connect('../../database/dbCardioBot.db')
    database = conn.cursor()

    # Execute a query to fetch all posts
    database.execute("SELECT * FROM Kits")

    # Fetch all the rows
    rows = database.fetchall()

    # Close the cursor and connection
    database.close()
    conn.close()

    # Convert the rows to a list of dictionaries
    posts = [{"ID": row[0], "item_sku": row[1].split(', '), "assembly_position": row[2]} for row in rows]

    return posts


# Endpoint para fazer um get em id único 
@app.get("/posts/{post_id}")
def read_post(post_id: int):
 # Establish a new connection
    conn = connect('../../database/dbCardioBot.db')
    database = conn.cursor()

    # Execute a query to fetch the post with the specified ID
    database.execute("SELECT * FROM Kits WHERE ID = ?", (post_id,))
    row = database.fetchone()

    # Close the cursor and connection
    database.close()
    conn.close()

    # If the row is found, return the post as a dictionary
    if row:
        post = {"ID": row[0], "item_sku": row[1].split(', '), "assembly_position": row[2]}
        return post
    else:
        # If the row is not found, raise HTTPException with 404 status code
        raise HTTPException(status_code=404, detail="Post not found")



# Endpoint de update de um kit 
@app.put("/posts/{post_id}")
def update_post(post_id: int, post_data: Post):
  # Establish a new connection
    conn = connect('../../database/dbCardioBot.db')
    database = conn.cursor()

    post_dict = post_data.dict()
    # Execute a query to check if the post exists
    database.execute("SELECT * FROM Kits WHERE ID = ?", (post_id,))
    existing_post = database.fetchone()

    # Função para criar uma entrada no arquivo de logs

    def log_update_time(post_id: int):
        # Padrão da entrada no log
        log_entry = {
            "user": "admin",
            "activity": "editar",
            "kit": post_id,
            "hour": datetime.now().strftime("%H:%M"),
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        # Abrir o arquivo JSON
        with open("../dashboard/user.activities.json", "r+") as file:
            # Carregar o conteúdo do arquivo JSON em um dicionário
            data = json.load(file)
            
            # Obter o próximo ID para o novo log
            next_id = str(len(data["logs"]) + 1)
            
            # Adicionar o novo log ao dicionário "logs"
            data["logs"][next_id] = log_entry
            
            # Voltar para o início do arquivo
            file.seek(0)
            
            # Escrever o dicionário atualizado de volta no arquivo JSON
            json.dump(data, file, indent=4)
            
            # Truncar o arquivo para remover qualquer conteúdo excedente
            file.truncate()

    if existing_post:
        log_update_time(post_id)
        # Execute a query to update the post
        database.execute("UPDATE Kits SET Item_SKUs = ?, Kit_assembly_positions = ? WHERE ID = ?", (', '.join(post_data.Item_SKUs), post_data.Kit_assembly_positions, post_id))
        # Commit the changes
        conn.commit()
        # Close the cursor and connection
        database.close()
        conn.close()

        return {"message": "Kit atualizado", "kit_id": post_id, **post_dict}
    else:
        # Close the cursor and connection
        database.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Kit não encontrado")


# Para rodar o código, basta rodar o comando "uvicorn warehouse:app --reload" no terminal.