from tinydb import TinyDB

# Create or connect to the TinyDB database
db = TinyDB('log_kits_items.json')

# Clear the existing database to avoid duplicates
db.drop_tables()

# Create the items and kits tables
itens_table = db.table('itens')
kits_table = db.table('kits')

# Populate the items table with item data
itens_data = [
    {'id': 1, 'nome': 'Item A'},
    {'id': 2, 'nome': 'Item B'},
    {'id': 3, 'nome': 'Item C'},
    {'id': 4, 'nome': 'Item D'},
    {'id': 5, 'nome': 'Item E'},
    # Continue adding more items as needed...
]

itens_table.insert_multiple(itens_data)

# Populate the kits table with kit data, including item IDs and manually set creation dates
kits_data = [
    {'id': 1, 'numero_do_kit': 1, 'itens': [1, 1, 2, 3, 3, 3], 'date_created': '2024-03-27'},  # Today
    {'id': 2, 'numero_do_kit': 2, 'itens': [4, 4, 5], 'date_created': '2024-03-25'},  # This week
    {'id': 3, 'numero_do_kit': 3, 'itens': [2, 3, 1, 1], 'date_created': '2024-03-20'},  # This month
    {'id': 4, 'numero_do_kit': 1, 'itens': [1, 1, 2, 3, 3, 3], 'date_created': '2024-03-15'},  # This month
    {'id': 5, 'numero_do_kit': 5, 'itens': [2, 2, 2, 3, 1], 'date_created': '2024-02-15'},  # Earlier this year
    {'id': 6, 'numero_do_kit': 6, 'itens': [1, 2, 3, 4], 'date_created': '2024-01-10'},  # Earlier this year
    # Continue adding more kits as needed...
]

kits_table.insert_multiple(kits_data)