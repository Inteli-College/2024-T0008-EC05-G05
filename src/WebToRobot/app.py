from fastapi import FastAPI, Request, Form, Depends, HTTPException
from tinydb import TinyDB, Query
from dobot import Dobot
from qreader import QReader
import cv2
import os
from datetime import datetime

app = FastAPI()

dobot = Dobot()

qreader = QReader()


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

# http://127.0.0.1:8000/conectar_dobot/mover_para_posicoes/?posicao_inicial=A1&posicao_final=A2
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
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança baixa: {e}"}
    

    try :
        dobot.mover_para(seguranca_alta['x'], seguranca_alta['y'], seguranca_alta['z'], seguranca_alta['r'])
    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição de segurança alta: {e}"}
    

    # Foto de escaneamento do QRcode

    dados_qr = await capturar_qr_code()

    # dados_ultrasoico = await capturar_dados_ultrassonico()

    # if dados_ultrasoico > 10:
    #     return {"status": "erro", "mensagem": "Item não foi pego {e}"}
    #     status_ultrasoico = "Item não foi pego, distancia: " + str(dados_ultrasoico)
    # else:
    #     status_ultrasoico = "Item foi pego, distancia: " + str(dados_ultrasoico)
    #     return {"status": "sucesso", "mensagem": "Item pego com sucesso."}


    seguranca_baixa = posicao_seguranca_baixa[0]
    try :
        dobot.mover_para(seguranca_baixa['x'], seguranca_baixa['y'], seguranca_baixa['z'], seguranca_baixa['r'])
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
    except Exception as e: 
        print(f"Erro ao mover para a posição final: {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição inicial: {e}"}
    
    return {"status": "sucesso", "dados_qr": dados_qr}
    

@app.get('/capturar')
async def capturar_qr_code():
    # Capture an image from the webcam
    camera = cv2.VideoCapture(1)
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