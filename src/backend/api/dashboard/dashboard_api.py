from typing import List
from datetime import datetime, timedelta
from collections import defaultdict
from fastapi import FastAPI
from tinydb import TinyDB, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db_kits = TinyDB('log_kits_items.json')
db_actions = TinyDB('user_activities.json')


app.add_middleware(
    CORSMiddleware,
    # Definindo as origens que podem fazer requisições
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
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
