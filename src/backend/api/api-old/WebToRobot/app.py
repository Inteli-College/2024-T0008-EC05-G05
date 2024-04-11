from fastapi import FastAPI, Request, Form, Depends, HTTPException
from tinydb import TinyDB, Query
from dobot import Dobot
from qreader import QReader
import cv2
import os
from datetime import datetime
from pydantic import BaseModel
import httpx
import time
import json
import sqlite3
import socket

def ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        print("IP Address:", ip_address)
        print(f"localhost: http://{ip_address}")
        return ip_address
    except Exception as e:
        return "Não foi possível obter o IP: " + str(e)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Inicializa a classe Dobot
dobot = Dobot()

# Inicializa o QReader
qreader = QReader()

# Vatriaveis do sensor de ultrassom
ativacao_sensor = False
data_recebida = ""

# Modelo de dados para a entrada de dados Raspberry Pi Pico
class PicoData(BaseModel): # BaseModel para validar e tratar dados JSON recebidos automaticamente
    pegou: str

# Inicializa o banco de dados
# db = TinyDB('db.json', indent=4)
# itens = db.table('Itens')
# kits = db.table('Kits')
# positions = db.table('Positions')

# Exemplo de inserção de dados no banco de dados
# itens.insert({'item_code': '123', 'name': 'Seringa', 'initial_position': 'A1', 'final_position': 'B2'})
# kits.insert({'kit_code': 'K1', 'name': 'Kit Cirurgia', 'items': ['123', '456']})
# positions.insert({'position_code': 'A1', 'x': 10, 'y': 20, 'z': 30, 'r': 5})
    
conn = sqlite3.connect('../../database/dbCardioBot.db')
cursor = conn.cursor()   

def inserir_item(sku, name, position_name):
    cursor.execute("INSERT INTO Items (SKU, Name, Position_name) VALUES (?, ?, ?)", (sku, name, position_name))
    conn.commit()

# Buscar dados
def buscar_item(sku):
    cursor.execute("SELECT * FROM Items WHERE SKU = ?", (sku,))
    print(f"SELECT * FROM Items WHERE SKU = {sku}")
    return cursor.fetchone()

def buscar_kit(KitID):
    cursor.execute("SELECT * FROM Kits WHERE ID = ?", (KitID,))
    print(f"SELECT * FROM Kits WHERE ID = {KitID}")
    return cursor.fetchone()

def buscar_posicao(PosicaoName):
    cursor.execute("SELECT * FROM Position WHERE Position_name = ?", (PosicaoName,))
    print(f"SELECT * FROM Position WHERE Position_name = {PosicaoName}")
    return cursor.fetchone()

def atualizar_posicao(PosicaoName, x, y, z, r):
    cursor.execute("UPDATE Position SET x = ?, y = ?, z = ?, r = ? WHERE Position_name = ?", (x, y, z, r, PosicaoName))
    conn.commit()

def inserir_posicao(PosicaoName, x, y, z, r):
    cursor.execute("INSERT INTO Position (Position_name, x, y, z, r) VALUES (?, ?, ?, ?, ?)", (PosicaoName, x, y, z, r))
    conn.commit()

# Codio de execução da API do FastAPI: uvicorn app:app --host 0.0.0.0 --reload --port 80

# IPV4 do seu computador
ip_servidor = ip_address()

# Middleware para log das requisições
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.now()
    
    # Processa a requisição
    response = await call_next(request)

    app_username = "Placeholder"
    
    # Captura informações da requisição
    request_info = {
        "timestamp": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "client_ip": request.client.host,
        "user_agent": request.headers.get("user-agent", "n/a"),
        "username": app_username,
        "method": request.method,
        "url": request.url.path,
        "query_params": dict(request.query_params)
        }
    
    try:
        with open("request_log.json", "r+") as log_file:
            log_file.seek(0, 2)  # Vai para o final do arquivo
            if log_file.tell() == 0:
                # Arquivo está vazio
                log_file.write(json.dumps([request_info]))
            else:
                log_file.seek(0, 2)  # Move para o final novamente
                # Apagar ] e adicionar uma nova entrada
                log_file.seek(log_file.tell() - 1, os.SEEK_SET)
                log_file.write(', ' + json.dumps(request_info) + ']')
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo
        with open("request_log.json", "w") as log_file:
            log_file.write(json.dumps([request_info]))
    
    return response

# Endpoint para testar a conexão com o dobot
# http://IPV4 do seu computador/conectar_dobot/?porta=COM6
@app.get('/conectar_dobot/')
async def conectar_dobot(porta: str):
    print(f"Tentando conectar ao dobot na porta {porta}.")
    try:
        dobot.conectar_dobot(porta)
        print("Conectado ao dobot com sucesso.")
        return {"status": "sucesso", "mensagem": "Conectado ao dobot com sucesso."}
    except Exception as e:
        print(f"Falha ao conectar ao robô: {e}")
        return {"status": "erro", "mensagem": f"Falha ao conectar ao robô: {e}"}

# Função para mover o dobot para uma posição
def mover_para_posicao(posicaoCod, atuador=None, estado_atuador=None):
    posicao = buscar_posicao(posicaoCod)

    print(f"Movendo para a posição {posicao}...")

    # posicao = posicao[0]

    if not posicao:
        print("Posição não encontrada.")
        raise HTTPException(status_code=404, detail="Posição não encontrada")

    try:
        dobot.mover_para(posicao[1], posicao[2], posicao[3], posicao[4])

        # Se não tiver parametos do atuador, o braço do dobot vai apenas para a posição
        if atuador is not None and estado_atuador is not None:
            dobot.atuador(atuador, estado_atuador)

    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição: {posicaoCod} : {e}"}

# Endpoint para testar a desconexão com o dobot
# http://IPV4/mover_para_posicoes/?posicao_inicial=A1&posicao_final=A2
@app.get('/mover_para_posicoes/')
async def mover_para_posicoes(posicao_inicial: str, posicao_final: str):
    
    print(f"Movendo dobot para as posições {posicao_inicial} e {posicao_final}.")

    # While loop para tentar pegar o item durante um certo número de tentativ

    tentativas = 0
    while tentativas < 3:

        mover_para_posicao('posicaoVerificacaoAlta')

        mover_para_posicao(posicao_inicial, "suck", "On")
        
        mover_para_posicao('posicaoVerificacaoAlta')
        
        mover_para_posicao('posicaoVerificacaoBaixa', "suck", "Off")

        mover_para_posicao('posicaoVerificacaoAlta')
        
        async with httpx.AsyncClient() as client:
            await client.get(f"http://{ip_servidor}/ativar_sensor")

        if data_recebida == "True":
            # print(f'Valor data_recebida (funcao mover posicoes): {data_recebida}')
            print("Item foi pego") 

            break
        else:
            # Robo vai tentar pegar o item novamente
            # print(f'Valor data_recebida (funcao mover posicoes): {data_recebida}')    

            tentativas += 1
            print("Item não foi pego!")   
    
    # Foto de escaneamento do QRcode
    dados_qr = await capturar_qr_code()

    # Levar o item a posicação final dele
    mover_para_posicao('posicaoVerificacaoBaixa', "suck", "On")

    mover_para_posicao('posicaoVerificacaoAlta')

    mover_para_posicao(posicao_final, "suck", "Off")

    return {"status": "sucesso", "dados_qr": dados_qr, "dados_ultra": data_recebida}
    

@app.get('/capturar')
async def capturar_qr_code():
    # Captura uma imagem da webcam
    camera = cv2.VideoCapture(1)
    _, image = camera.read()
    camera.release()

    # Salva a imagem
    cv2.imwrite("qrcode.png", image)

    # Pega a imagem salva
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Usa a função detect_and_decode para decodificar o qr code
    decoded_text = qreader.detect_and_decode(image=image)

    # Retorna os dados do qr code
    return {'Dados': decoded_text}


# Endpoint de post para o Rasp mandar os dados
@app.post("/pico_data")
async def receive_pico_data(data: PicoData):
    global data_recebida
    data_recebida = data.pegou
    # print(f"DATA Rasp Pico (pico_data endpoint): Status={data_recebida}")
    return {"status": "Dados recebidos"}

# Endpoint para pegar os últimos dados do Raspberry Pi Pico
@app.get("/pico_data")
async def get_pico_data():
    if data_recebida is not None:
        # print(f"DATA Rasp Pico (get_pico_data endpoint): Status={data_recebida}")
        return {"data": data_recebida}
    else:
        return {"error": "Nenhum dado disponível"}

# Endpoint para rodar a montagem de um kit
# http://IP/montar_kit/?kit_code=K1
@app.get("/montar_kit/")
async def montar_kit(kit_code: str):
    # Buscar o kit no banco de dados
    kit = buscar_kit(kit_code)
    print(kit)

    numero_de_items = 2

    if not kit:
        raise HTTPException(status_code=404, detail="Kit não encontrado")

    # Resposta SQL query: 1, "Luva, Vazio, Luftal, Vazio, Vazio, Caixa, Vazio, Vazio", frente
    lista_itens = kit[1].split(", ")
    posicao_final = kit[2]
    print(f"Lista de items: {lista_itens}")

    # Montar o kit interando por cada item
    for item in lista_itens:
        if item != "Vazio":
            print(f"Item: {item}")

            item_name = buscar_item(item)[1]
            posicao = buscar_item(item)[2]

            for i in numero_de_items: 
                # Buscar o item no banco de dados

                if not item:
                    raise HTTPException(status_code=404, detail="Item não encontrado")
                
                # Mover o dobot para a posição inicial do item
                print(f"Pegando o item: {item_name}...")
                

                # Rodar a sequência de movimentos pelo endpoint /mover_para_posicoes/
                await mover_para_posicoes(posicao, posicao_final)

# Endpoint para salvar uma posição
# http://10.128.0.8/salvar_posicao/?position_code=P1
@app.get('/salvar_posicao/')
async def salvar_posicao(position_code: str,):
    # Verificar se existe uma posição com o mesmo nome
    posicao = buscar_posicao(position_code)

    dobot_pos = dobot.obter_posicao()

    # Se a posição já existir, atualizar a posição
    if posicao:
        print(dobot_pos)
        # Atualizar a posição
        atualizar_posicao(position_code, dobot_pos[0], dobot_pos[1], dobot_pos[2], dobot_pos[3])
        return {"status": "sucesso", "mensagem": "Posição atualizada com sucesso."}
    else:
        print(dobot_pos)

        # Inserir a nova posição
        inserir_posicao(position_code, dobot_pos[0], dobot_pos[1], dobot_pos[2], dobot_pos[3])

        return {"status": "sucesso", "mensagem": "Posição salva com sucesso."}
    
