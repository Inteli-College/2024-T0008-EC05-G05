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
db = TinyDB('db.json', indent=4)
itens = db.table('Itens')
kits = db.table('Kits')
positions = db.table('Positions')

# Exemplo de inserção de dados no banco de dados
# itens.insert({'item_code': '123', 'name': 'Seringa', 'initial_position': 'A1', 'final_position': 'B2'})
# kits.insert({'kit_code': 'K1', 'name': 'Kit Cirurgia', 'items': ['123', '456']})
# positions.insert({'position_code': 'A1', 'x': 10, 'y': 20, 'z': 30, 'r': 5})

# Codio de execução da API do FastAPI: uvicorn app:app --host 0.0.0.0 --reload --port 80

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
    posicao = positions.search(Query().position_code == posicaoCod)

    posicao = posicao[0]

    if not posicao:
        print("Posição não encontrada.")
        raise HTTPException(status_code=404, detail="Posição não encontrada")

    try:
        dobot.mover_para(posicao['x'], posicao['y'], posicao['z'], posicao['r'])

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
            await client.get("http://10.128.0.8/ativar_sensor")

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
    kit = kits.search(Query().kit_code == kit_code)
    print(kit)

    if not kit:
        raise HTTPException(status_code=404, detail="Kit não encontrado")

    # Montar o kit interando por cada item
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

# Endpoint para salvar uma posição
# http://10.128.0.8/salvar_posicao/?position_code=P1
@app.get('/salvar_posicao/')
async def salvar_posicao(position_code: str,):
    # Verificar se existe uma posição com o mesmo nome
    posicao = positions.search(Query().position_code == position_code)

    dobot_pos = dobot.obter_posicao()

    # Se a posição já existir, atualizar a posição
    if posicao:
        print(dobot_pos)
        # Atualizar a posição
        positions.update({'position_code': position_code, 'x': dobot_pos[0], 'y': dobot_pos[1], 'z': dobot_pos[2], 'r': dobot_pos[3]}, Query().position_code == position_code)
        return {"status": "sucesso", "mensagem": "Posição atualizada com sucesso."}
    else:
        print(dobot_pos)

        positions.insert({'position_code': position_code, 'x': dobot_pos[0], 'y': dobot_pos[1], 'z': dobot_pos[2], 'r': dobot_pos[3]})

        return {"status": "sucesso", "mensagem": "Posição salva com sucesso."}
    

# !!! ENDPOINTS DE TESTE DE OUTRA ABORDAGEM PARA A CONEXÃO COM O RASPBERRY PI PICO !!!

# # Endpoint para receber dados do Raspberry Pi Pico
# @app.post("/pico_data")
# async def receive_pico_data(data: PicoData):
#     # Processar ou salvar os dados recebidos

#     global data_recebida
#     data_recebida = data.pegou

#     print(f"DATA Rasp Pico (pico_data endpoint): Status={data_recebida}")

#     return {data_recebida}

# @app.get("/check")
# async def check_activation():
#     global ativacao_sensor
#     print(f"Status do ativacao_sensor (Funcao Check): {ativacao_sensor}")

#     if ativacao_sensor:
#         async with httpx.AsyncClient() as client:
#             await client.get("http://10.128.0.8/ativar_sensor")

#         return "Ativar"
#     else:
#         async with httpx.AsyncClient() as client:
#             await client.get("http://10.128.0.8/desativar_sensor")
#         return "Espere"

# @app.get("/ativar_sensor")
# async def ativar_sensor():
#     # print("Ativar sensor Endpoint")
#     global ativacao_sensor
#     ativacao_sensor = True
#     return {"message": "Sensor ativado"}

# @app.get("/desativar_sensor")
# async def desativar_sensor():
#     # print("Desativar sensor Endpoint")
#     global ativacao_sensor
#     ativacao_sensor = False
#     return {"message": "Sensor desativado"}
