import pydobot
from serial.tools import list_ports
import time, inquirer, typer
from yaspin import yaspin


# Instanciar o typer para criar o CLI
app = typer.Typer()

def incializar_programa():
    spinner = yaspin(text="Inicializando o programa...", color="yellow")
    spinner.start()
    time.sleep(2)
    spinner.stop()
    
    print("Seleciona a opção desejada.")


def conectar_dobot():
    portas_disponiveis = list_ports.comports()

    portas = [x.device for x in portas_disponiveis]

    print(f'Portas disponiveis: {[x.device for x in portas_disponiveis]}')

    opcoes = [
    inquirer.List("Porta", message="Qual porta deseja conectar", choices=[x for x in portas if "ttyUSB" in x or "COM" in x
    ])
    ]

    resposta = inquirer.prompt(opcoes)
    port = resposta["Porta"]

    print(f"Conectando ao dobot na porta: {resposta}")

    if not portas_disponiveis:
        print("Sem portas de conexão disponíveis.")
        return None
    
    # port = portas_disponiveis[0].device

    # print(f"Conectando ao dobot na porta: {port}")

    try:
        device = pydobot.Dobot(port=port, verbose=False)
        print("Conectado ao dobot com sucesso.")
        return device
    except Exception as e:
        print("Falha ao conectar ao robô:" + str({e}))
        return None

def desconectar_robot(device):
    if device:
        try:
            device.close()
            print("Disconectado do dobot com sucesso.")
        except Exception as e:
            print("Erro ao desconectar:" + str({e}))
    else:
        print("Não há conexão com o dobot.")

def mover(device, x, y, z, r):
    if device:
        try:
            spiner = yaspin(text="Movendo o braço robotico...", color="yellow")

            spiner.start()
            device.move_to(x, y, z, r, wait=True)

            spiner.stop()

            print(f"Braço robotico movido para: ({x}, {y}, {z}, {r})")

        except Exception as e:
            print("Erro ao mover o braço" + str({e}))
    else:
        print("Conecte ao dobot primeiro.")

def atuador(device):

    opcoesAcao = [
        inquirer.List("Ação", message="Qual ação deseja realizar?", choices=["suck", "grip"])
        ]
    
    respostaAcao = inquirer.prompt(opcoesAcao)
    respostaAcao = respostaAcao["Ação"]

    opcoesEstado = [
    inquirer.List("Estado", message="Ligar ou Desligar?", choices=["On", "off"])
    ]

    respostaEstado = inquirer.prompt(opcoesEstado)
    respostaEstado = respostaEstado["Estado"]

    if device:
        try:
            if respostaAcao == "suck":
                if respostaEstado == "On":
                    device.suck(True)
                else:
                    device.suck(False)
            elif respostaAcao == "grip":
                if respostaEstado == "On":
                    device.suck(True)
                else:
                    device.suck(False)
        except Exception as e:
            print("Erro na ação:" + str({e}))


def main():
    dobot_conectado = None
    continuar_prorgama = True

    incializar_programa()

    while continuar_prorgama:

        opcoes = [
            inquirer.List("Comando", message="Qual comando deseja realizar?", choices=["Conectar", "Disconectar", "Mover","Atuador", "Sair"])
            ]
        
        print("teste" + str(opcoes))

        resposta = inquirer.prompt(opcoes)
        resposta = resposta["Comando"]

        # Verifica qual comando foi escolhido
        if resposta == "Conectar":
            dobot_conectado = conectar_dobot()
        
        elif resposta == "Disconectar":
            desconectar_robot(dobot_conectado)
            dobot_conectado = None
        
        elif resposta == "Mover":
            if dobot_conectado:
                x = float(input("X "))
                y = float(input("Y"))
                z = float(input("Z"))
                r = float(input("R"))
                mover(dobot_conectado, x, y, z, r)
            else:
                print("Please connect to Dobot first.")

        elif resposta == "Atuador":
            if dobot_conectado:
                atuador(dobot_conectado)
            else:
                print("Please connect to Dobot first.")
        
        elif resposta == "Sair":
            desconectar_robot(dobot_conectado)
            print("Exiting program.")
            break
        else:
            print("Invalid command.")

        # continuar_prorgama = typer.confirm("Deseja continuar?") 

if __name__ == "__main__":
    main()
