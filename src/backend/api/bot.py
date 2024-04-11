try:
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi import FastAPI, Request, HTTPException
    import socket, sqlite3, json, os, httpx, cv2
    from  modules import Dobot
    from pydantic import BaseModel
    from datetime import datetime, timedelta
    from typing import List
    from qreader import QReader
    from collections import defaultdict
    from tinydb import TinyDB, Query
    print("Dependências importadas com sucesso")
except ImportError as e:
    print(e)

# Create a FastAPI app

# Inicializa a aplicação FastAPI
app = FastAPI()

# Inicializa a classe Dobotr
dobot = Dobot()

# Inicializa o QReader
qreader = QReader()

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
    

# Vatriaveis do sensor de ultrassom
ativacao_sensor = False
data_recebida = ""

app.add_middleware(
    CORSMiddleware,
    # Definindo as origens que podem fazer requisições
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


#Sistema de Logs
db_logs_bot = TinyDB('../logs-db/bot-log.json', indent=4)

# Função para adicionar logs
def add_log(message):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_logs_bot.insert({'date': current_date, 'user_action': message})

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
    
conn = sqlite3.connect('../database/dbCardioBot.db')
cursor = conn.cursor()   

def inserir_item(sku, name, position_name):
    cursor.execute("INSERT INTO Items (SKU, Name, Position_name) VALUES (?, ?, ?)", (sku, name, position_name))
    conn.commit()

# Buscar dados
def buscar_item(sku):
    cursor.execute("SELECT * FROM Items WHERE Name = ?", (sku,))
    print(f"SELECT * FROM Items WHERE Name = {sku}")
    return cursor.fetchone()

def buscar_kit(KitID):
    cursor.execute("SELECT * FROM Kits WHERE ID = ?", (KitID,))
    # print(f"SELECT * FROM Kits WHERE ID = {KitID}")
    return cursor.fetchone()

def buscar_posicao(PosicaoName):
    cursor.execute("SELECT * FROM Position WHERE Position_name = ?", (PosicaoName,))
    # print(f"SELECT * FROM Position WHERE Position_name = {PosicaoName}")
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

    requests_logs = TinyDB('../database/request_log.json', indent=4, sort_keys=True)

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
        requests_logs.insert(request_info)
    except Exception as e:
        # Se o arquivo não existir, cria um novo
        with open("../database/request_log.json", "+a") as log_file:
            log_file.write(json.dumps([request_info]))

    return response

# Endpoint para conectar ao dobot automaticamente
@app.get('/conectar_dobot/')
async def conectar_dobot():
    try:
        # Conectar ao dobot, com a porta, velocidade e aceleração
        dobot.conectar_dobot()
        print("Conectado ao dobot com sucesso.")
        add_log("Conectado ao dobot com sucesso.")
        return {"status": "sucesso", "mensagem": "Conectado ao dobot com sucesso."}
    except Exception as e:
        print(f"Falha ao conectar ao robô: {e}")
        add_log(f"Falha ao conectar ao robô: {e}")
        return {"status": "erro", "mensagem": f"Falha ao conectar ao robô: {e}"}

# Endpoint para conectar ao dobot com a porta especificada
@app.get('/conectar_dobot_porta/')
async def conectar_dobot_porta(porta: str):
    try:
        # Conectar ao dobot
        dobot.conectar_dobot_porta(porta)
        print("Conectado ao dobot com sucesso.")
        add_log(f"Dobot conectado a porta: {porta}.")
        return {"status": "sucesso", "mensagem": "Conectado ao dobot com sucesso."}
    except Exception as e:
        print(f"Falha ao conectar ao robô: {e}")
        add_log(f"Falha ao conectar na porta: {e}")
        return {"status": "erro", "mensagem": f"Falha ao conectar ao robô: {e}"}

# Função para mover o dobot para uma posição
def mover_para_posicao(posicaoCod, atuador=None, estado_atuador=None):
    posicao = buscar_posicao(posicaoCod)
    add_log(f"Movendo para a posição {posicao}...")

    print(f"Movendo para a posição {posicao}...")

    # posicao = posicao[0]

    if not posicao:
        print("Posição não encontrada.")
        add_log(f"O robô não conseguiu encontrar a posição: {posicao}.")
        raise HTTPException(status_code=404, detail="Posição não encontrada")

    try:
        dobot.mover_para(posicao[1], posicao[2], posicao[3], posicao[4])

        # Se não tiver parametos do atuador, o braço do dobot vai apenas para a posição
        if atuador is not None and estado_atuador is not None:
            dobot.atuador(atuador, estado_atuador)

    except Exception as e: 
        print(f"Erro ao mover para a posição inicial: {e}")
        add_log(f"Erro ao mover para a posição: {posicaoCod} : {e}")
        return {"status": "erro", "mensagem": f"Erro ao mover para a posição: {posicaoCod} : {e}"}

# Endpoint para testar a desconexão com o dobot
# http://IPV4/mover_para_posicoes/?posicao_inicial=A1&posicao_final=A2
@app.get('/mover_para_posicoes/')
async def mover_para_posicoes(posicao_inicial: str, posicao_final: str):
    
    print(f"Movendo dobot para as posições {posicao_inicial} e {posicao_final}.")
    add_log(f"Movendo dobot para as posições {posicao_inicial} e {posicao_final}.")

    # While loop para tentar pegar o item durante um certo número de tentativ

    tentativas = 0
    while tentativas < 3:
        # dobot.velocidade(500, 100)
        mover_para_posicao('posicaoVerificacaoAlta')

        mover_para_posicao(posicao_inicial, "suck", "On")
        
        mover_para_posicao('posicaoVerificacaoAlta')
        
        mover_para_posicao('posicaoVerificacaoBaixa', "suck", "Off")

        mover_para_posicao('posicaoVerificacaoAlta')
        
        async with httpx.AsyncClient() as client:
            await client.get(f"http://{ip_servidor}:8800/pico_data")
        print(data_recebida)
        if data_recebida == "True":
            # print(f'Valor data_recebida (funcao mover posicoes): {data_recebida}')
            print("Item foi pego") 
            add_log("Item foi pego")

            break
        else:
            # Robo vai tentar pegar o item novamente
            # print(f'Valor data_recebida (funcao mover posicoes): {data_recebida}')    

            tentativas += 1
            print("Item não foi pego!")
            add_log("Item não foi pego!")  
    
    # Foto de escaneamento do QRcode
    dados_qr = await capturar_qr_code()

    # Salvar infor do qr code em json

    with open('dados_qr.json', 'w') as arquivo_json:
        json.dump(dados_qr, arquivo_json)

    # Levar o item a posicação final dele
    mover_para_posicao('posicaoVerificacaoBaixa', "suck", "On")

    mover_para_posicao('posicaoVerificacaoAlta')

    mover_para_posicao(posicao_final, "suck", "Off")

    add_log(f"Foi possível ler o qr code: {dados_qr} e o sensor ultrassônico recebeu: {data_recebida}")
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
async def montar_kit(kit_code):
    # Buscar o kit no banco de dados
    print(f"Montando o kit {kit_code}...")
    add_log(f"O robô está montando o kit {kit_code}...")
    kit = buscar_kit(kit_code)
    print(kit)

    numero_de_items = 1

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

            item_name = buscar_item(item)
            print(f"Item inteiro 3123: {item_name}")
            item_name = item_name[1]
            print(f"Item: {item_name}")
            posicao = buscar_item(item)
            posicao = posicao[2]
            print(f"Posicao: {posicao}")

            for i in range(0,numero_de_items): 
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
        add_log(f"A posição do item foi atualizada: {position_code}.")
        return {"status": "sucesso", "mensagem": "Posição atualizada com sucesso."}
    else:
        print(dobot_pos)

        # Inserir a nova posição
        inserir_posicao(position_code, dobot_pos[0], dobot_pos[1], dobot_pos[2], dobot_pos[3])
        add_log(f"Uma nova posição foi criada: {position_code}.")


        return {"status": "sucesso", "mensagem": "Posição salva com sucesso."}
    

if __name__ == "__main__":
    try:
        dobot.conectar_dobot()

        import uvicorn
        uvicorn.run(app, host=ip_servidor, port=8800)
    except ImportError as e:
        print(e)