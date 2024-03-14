from fastapi import FastAPI, Request, Form, Depends, HTTPException
from tinydb import TinyDB, Query
from dobot import Dobot
from qreader import QReader
import cv2
import os
from datetime import datetime
from pydantic import BaseModel
import httpx

app = FastAPI()

dobot = Dobot()

qreader = QReader()

ativacao_sensor = False
data_recebida = ""

# Modelo de dados para a entrada de dados Raspberry Pi Pico
class PicoData(BaseModel): # BaseModel para validar e tratar dados JSON recebidos automaticamente
    pegou: str

# Inicializa o banco de dados
db = TinyDB('db.json', indent=4)
itens = db.table('Itens')
kits = db.table('Kits')
positions = db.table('Positions')

# itens.insert({'item_code': '123', 'name': 'Seringa', 'initial_position': 'A1', 'final_position': 'B2'})
# kits.insert({'kit_code': 'K1', 'name': 'Kit Cirurgia', 'items': ['123', '456']})
# positions.insert({'position_code': 'A1', 'x': 10, 'y': 20, 'z': 30, 'r': 5})

# Codio de execução da API do FastAPI - unvicorn app:app --reload

# http://127.0.0.1:8000/conectar_dobot/?porta=COM6
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

# http://127.0.0.1:8000/mover_para_posicoes/?posicao_inicial=A1&posicao_final=A2
@app.get('/mover_para_posicoes/')
async def mover_para_posicoes(posicao_inicial: str, posicao_final: str):
    print(f"Movendo dobot para as posições {posicao_inicial} e {posicao_final}.")
    posicao_inicial_data = positions.search(Query().position_code == posicao_inicial)
    posicao_final_data = positions.search(Query().position_code == posicao_final)

    posicao_seguranca_alta = positions.search(Query().position_code == 'posicaoVerificacaoAlta')
    posicao_seguranca_baixa = positions.search(Query().position_code == 'posicaoVerificacaoBaixa')

    if not posicao_inicial_data or not posicao_final_data:
        print("Posição não encontrada.")
        raise HTTPException(status_code=404, detail="Posição não encontrada")

    # Movendo para a posição inicial
    inicial = posicao_inicial_data[0]

    try :
        dobot.mover_para(inicial['x'], inicial['y'], inicial['z'], inicial['r'])
        dobot.atuador("suck", "On")
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição inicial: {e}"}
    
    # Posições de segurança

    seguranca_alta = posicao_seguranca_alta[0]
    try :
        dobot.mover_para(seguranca_alta['x'], seguranca_alta['y'], seguranca_alta['z'], seguranca_alta['r'])
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança alta: {e}"}
    

    seguranca_baixa = posicao_seguranca_baixa[0]
    try :
        dobot.mover_para(seguranca_baixa['x'], seguranca_baixa['y'], seguranca_baixa['z'], seguranca_baixa['r'])
        dobot.atuador("suck", "Off")
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança baixa: {e}"}
    

    try :
        dobot.mover_para(seguranca_alta['x'], seguranca_alta['y'], seguranca_alta['z'], seguranca_alta['r'])
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança alta: {e}"}
    
    # Foto de escaneamento do QRcode

    async with httpx.AsyncClient() as client:
        await client.get("http://10.128.0.8/ativar_sensor")

    print(data_recebida)

    if data_recebida == "Pegou":
        print("Item não foi pego")
    else:
        print("Item foi pego!")

    async with httpx.AsyncClient() as client:
        await client.get("http://10.128.0.8/desativar_sensor")

    print(data_recebida)

    dados_qr = await capturar_qr_code()

    seguranca_baixa = posicao_seguranca_baixa[0]
    try :
        dobot.mover_para(seguranca_baixa['x'], seguranca_baixa['y'], seguranca_baixa['z'], seguranca_baixa['r'])
        dobot.atuador("suck", "On")
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança baixa: {e}"}

    try :
        dobot.mover_para(seguranca_alta['x'], seguranca_alta['y'], seguranca_alta['z'], seguranca_alta['r'])
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança alta: {e}"}

    # Movendo para a posição final
    final = posicao_final_data[0]
    try :
        dobot.mover_para(final['x'], final['y'], final['z'], final['r'])
        dobot.atuador("suck", "Off")
    except Exception as e: 
        print(f"Erro ao mover para a posição final: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição inicial: {e}"}
    
    return {"status": "sucesso", "dados_qr": dados_qr, "dados_ultra": data_recebida}
    

@app.get('/capturar')
async def capturar_qr_code():
    # Capture an image from the webcam
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    camera.release()

    # Save the image
    cv2.imwrite("qrcode.png", image)

    # Get the image that contains the QR code
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image)

    # Return the decoded text
    return {'Dados': decoded_text}

@app.get('/mostrar_dados_qr')
async def mostrar_dados_qr():
    # Return the dictionary containing QR code data
    return qr_code_data

# Endpoint para receber dados do Raspberry Pi Pico
@app.post("/pico_data")
async def receive_pico_data(data: PicoData):
    # Processar ou salvar os dados recebidos

    global data_recebida
    data_recebida = data.pegou

    print(f"Data Rasp Pico: Status={data.pegou}")

    return {data_recebida}

@app.get("/check")
async def check_activation():
    global ativacao_sensor
    print(f"Status do ativacao_sensor: {ativacao_sensor}")

    if ativacao_sensor:
        return "Ativar"
    else:
        return "Espere"

@app.get("/ativar_sensor")
async def ativar_sensor():
    global ativacao_sensor
    ativacao_sensor = True
    return {"message": "Sensor ativado"}

@app.get("/desativar_sensor")
async def desativar_sensor():
    global ativacao_sensor
    ativacao_sensor = False
    return {"message": "Sensor desativado"}

# Endpoint para rodar a montagem de um kit
# http://IP/montar_kit/?kit_code=K1
@app.get("/montar_kit/")
async def montar_kit(kit_code: str):
    # Buscar o kit no banco de dados
    kit = kits.search(Query().kit_code == kit_code)
    print(kit)

    if not kit:
        raise HTTPException(status_code=404, detail="Kit não encontrado")

    # Montar o kit
    for item_code in kit[0]['items']:
        # Buscar o item no banco de dados
        item = itens.search(Query().item_code == item_code)

        if not item:
            raise HTTPException(status_code=404, detail="Item não encontrado")
        
        # Mover o dobot para a posição inicial do item
        posicao_inicial = item[0]['initial_position']
        posicao_final = item[0]['final_position']
        item_name = item[0]['name']

        print(f"Pegando o item: {item_name}...")
        print(posicao_inicial)
        print(posicao_final)

        # Rodar a sequência de movimentos pelo endpoint /mover_para_posicoes/
        await mover_para_posicoes(posicao_inicial, posicao_final)



@app.get('/teste')
async def teste():
    return{"Dados": "Testeeeee"}


# uvicorn app:app --host 0.0.0.0 --reload --port 80