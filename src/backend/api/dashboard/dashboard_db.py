from tinydb import TinyDB, Query

# Criar ou conectar ao banco de dados TinyDB
db = TinyDB('db.json')

# Limpar o banco de dados existente para evitar duplicatas
db.drop_tables()

# Criação das tabelas de itens e kits
itens_table = db.table('itens')
kits_table = db.table('kits')

# Populando a tabela de itens com os dados dos itens
itens_data = [
    {'id': 1, 'nome': 'Item A'},
    {'id': 2, 'nome': 'Item B'},
    {'id': 3, 'nome': 'Item C'},
    {'id': 4, 'nome': 'Item D'},
    {'id': 5, 'nome': 'Item E'},
    # Pode continuar adicionando mais itens conforme necessário...
]

itens_table.insert_multiple(itens_data)

# Populando a tabela de kits com os dados dos kits, incluindo IDs de itens repetidos para indicar quantidade
kits_data = [
    {'id': 1, 'numero_do_kit': 1, 'itens': [1, 1, 2, 3, 3, 3]},  # Exemplo: 2x Item A, 1x Item B, 3x Item C
    {'id': 2, 'numero_do_kit': 2, 'itens': [4, 4, 5]},          # Exemplo: 2x Item D, 1x Item E
    {'id': 3, 'numero_do_kit': 3, 'itens': [2, 3, 1, 1]},       # Exemplo: 2x Item A, 1x Item B, 1x Item C
    {'id': 4, 'numero_do_kit': 4, 'itens': [5, 5, 5, 4]},       # Exemplo: 3x Item E, 1x Item D
    {'id': 5, 'numero_do_kit': 5, 'itens': [2, 2, 2, 3, 1]},    # Exemplo: 1x Item A, 3x Item B, 1x Item C
    # Pode continuar adicionando mais kits conforme necessário...
]

kits_table.insert_multiple(kits_data)
