import sqlite3
from tinydb import TinyDB

db_tinydb = TinyDB('db.json')
positions = db_tinydb.table('Positions').all()

conn = sqlite3.connect('../../database/dbCardioBot.db')
cursor = conn.cursor()


for pos in positions:
    position_data = pos.values()  # dicionário
    cursor.execute("""
    INSERT INTO Position (Position_name, x, y, z, r, Jump_factor) VALUES (?, ?, ?, ?, ?, ?)
    """, (*position_data, None))  # O 'None' é para o Jump_factor, já que não temos essa informação

# Confirmar as mudanças
conn.commit()

# Fechar a conexão
conn.close()