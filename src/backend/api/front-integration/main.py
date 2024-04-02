from typing import List
from datetime import datetime, timedelta
from collections import defaultdict
from fastapi import FastAPI
from tinydb import TinyDB, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tinydb import TinyDB, Query
from typing import List
from datetime import datetime
from sqlite3 import connect
from queue import Queue
import json
import os

# Inicia o servidor FastAPI

app = FastAPI()

# Inicia os logs de kits e itens
db_kits = TinyDB('log_kits_items.json')
db_actions = TinyDB('user_activities.json')

# Inicia o banco de dados com SQLite
conn = connect('../../database/dbCardioBot.db')
database = conn.cursor()


app.add_middleware(
    CORSMiddleware,
    # Definindo as origens que podem fazer requisições
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Modelo de dados para realizar o post nos logs
class KitSimple(BaseModel):
    numero_do_kit: int
    quantity: int

class ItemSimple(BaseModel):
    nome: str
    quantity: int
class Log(BaseModel):
    user: str
    activity: str
    kit: int
    hour: str
    date: str

######## Aqui estão as rotas da tela dashboard ########
def get_kits_in_date_range(period: str):
    kits_table = db_kits.table('kits')
    QueryObj = Query()
    today = datetime.now().date()

    if period == 'day':
        start_date = today
    elif period == 'week':
        start_date = today - timedelta(weeks=1)
    elif period == 'month':
        start_date = today - timedelta(days=30)
    elif period == 'year':
        start_date = today - timedelta(days=365)
    else:
        return []  # Invalid period

    filtered_kits = kits_table.search(QueryObj.date_created >= start_date.strftime('%Y-%m-%d'))

    aggregated_kits = defaultdict(lambda: {'quantity': 0, 'itens': [], 'date_created': '', 'ids': []})
    for kit in filtered_kits:
        kit_key = kit['numero_do_kit']
        aggregated_kits[kit_key]['quantity'] += 1

    kits_list = [KitSimple(numero_do_kit=numero, quantity=info['quantity']) for numero, info in aggregated_kits.items()]
    return kits_list

def get_items_in_date_range(period: str):
    kits_table = db_kits.table('kits')
    QueryObj = Query()
    today = datetime.now().date()

    if period == 'day':
        start_date = today
    elif period == 'week':
        start_date = today - timedelta(weeks=1)
    elif period == 'month':
        start_date = today - timedelta(days=30)
    elif period == 'year':
        start_date = today - timedelta(days=365)
    else:
        return []  # Invalid period

    filtered_kits = kits_table.search(QueryObj.date_created >= start_date.strftime('%Y-%m-%d'))

    item_counts = defaultdict(int)
    for kit in filtered_kits:
        for item_id in kit['itens']:
            item_counts[item_id] += 1

    itens_table = db_kits.table('itens')
    items_list = []
    for item_id, count in item_counts.items():
        item_record = itens_table.get(QueryObj.id == item_id)
        if item_record:  # Ensure the item exists
            items_list.append(ItemSimple(nome=item_record['nome'], quantity=count))
    
    return items_list

def get_logs(period: str) -> List[Log]:
    logs_table = db_actions.table('logs')
    QueryObj = Query()
    today = datetime.now().date()

    if period == 'day':
        start_date = today
    elif period == 'week':
        start_date = today - timedelta(weeks=1)
    elif period == 'month':
        start_date = today - timedelta(days=30)
    elif period == 'year':
        start_date = today - timedelta(days=365)
    else:
        return []  # Invalid period

    filtered_logs = logs_table.search(QueryObj.date >= start_date.strftime('%Y-%m-%d'))
    logs_list = [Log(**log_data) for log_data in filtered_logs]
    return logs_list

@app.get("/log/itens/{period}", response_model=List[ItemSimple])
async def get_items(period: str):
    items = get_items_in_date_range(period)
    print(items)
    return items

@app.get("/log/kits/{period}", response_model=List[KitSimple])
async def get_kits(period: str):
    kits = get_kits_in_date_range(period)
    print(kits)
    return kits

@app.get("/log/logs/{period}", response_model=List[Log])
async def get_log_entries(period: str):
    log_entries = get_logs(period)
    return log_entries

######## Aqui estão as rotas da tela supplies ########

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
    
    if existing_post:
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

# Função para criar uma entrada no arquivo de logs 

def log_update_time(post_id: int):
 
    windows_username = os.getenv('USERNAME')

    # Padrão da entrada no log
    log_entry = {"kit_id": post_id, "update_time": datetime.now().isoformat(), "windows_username": windows_username}

    with open("logs.json", "a", encoding="utf-8") as log_file:
        json.dump(log_entry, log_file, ensure_ascii=False)
        log_file.write("\n")


# Para rodar o código, basta rodar o comando "uvicorn warehouse:app --reload" no terminal.