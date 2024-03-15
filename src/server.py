from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
from modules import *


hydro = HydroDB(optional_path="src")

hydro.create(
    tables=["Positions", 'Itens', 'Kits'],
    columns=[
        ['position_name','x','y','z','r','j1','j2','j3','j4'],
        ['item_position', "item_name", 'item_code', "val"],
        ['kit_name', 'kit_itens', "kit_code", "kit_img", "kit_desc"]
    ],
    primary_key=['id', "item_code", 'kit_code']
)

start_spiner("Connecting Arm...", 1.5)
available_ports = list_ports.comports()
try :
    available_ports != []
    port = available_ports[0].device
    global bot # Globalize the variable 
    bot = CardioBot(port, False)

    success_message("Arm connected with success :)")

except Exception as e:
    fail_message('Non available ports')
        

server = Flask(__name__)
CORS(server, resources={r"/api/*": {"origins": "http://localhost:3000"}})
@server.route("/")
def _connect(): # Connects the bot to the computer
    return("BANANA")
    


@server.route('/api/get-positions')
def _get_position():
    try:
        table = hydro.get_table("Positions")
        return jsonify(table["rows"])  # Assuming "rows" contains the array of data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify([])  # Return an empty array if there is an error
    

@server.route('/api/get-itens')
def get_itens():
    try:
        table = hydro.get_table("Itens")
        return jsonify(table["rows"])  # Assuming "rows" contains the array of data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify([])  # Return an empty array if there is an error 
    

@server.route('/api/get-kits')
def get_kits():
    try:
        kits_table = hydro.get_table("Kits")
        return jsonify(kits_table["rows"])
    except Exception as e:
        print(f"ERROR ==> {e}")
        return jsonify([])


hydro.add(
    tables_names=["Kits", "Kits", "Kits"],
    into=(
        ["kit_name", "kit_itens", "Kit_code", "kit_img", "kit_desc"],
        ["kit_name", "kit_itens", "Kit_code", "kit_img", "kit_desc"],
        ["kit_name", "kit_itens", "Kit_code", "kit_img", "kit_desc"]
    ),
    values=(
        ["Kit_1", ["seringa", "agulha", "luvas"], 1, "logo192.png", "kit de uso geral"],
        ["Kit_2", ["luvas", "mascara", "protetor ocular", "touca"], 1, "logo192.png", "kit uso emergencia"],
        ["Kit_3", ["morfina", "agulha", "seringa"], 1, "logo192.png", "kit de anestesico"]
    )
)
server.run()
