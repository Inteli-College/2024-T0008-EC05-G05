from serial.tools import list_ports
import pydobot, json, sys, os


class CardioBot:
    def __init__(self) -> None:
        self.data_file_path = "src/data.json" # Caminho do arquivo JSON
        with open(self.data_file_path, "r") as data_file:  # Abre o arquivo em binário
            self.db = json.load(data_file)


    # Conecta o computador ao braço robótico
    def connect_arm(self):
        available_ports = list_ports.comports() # Verifica as portas do computador
        port = available_ports[0].device # Seta a porta disponível
        self.device = pydobot.Dobot(port=port, verbose=True) # Conecta ao braço à porta 
        self.prompt_commands(input("Commando : ").upper()) # Inicia os comandos po CLI


    # Acessa os daos de posições do arquivo JSON
    def open_data(self, position: int):
        positions = self.db["Positions"]
        initial_position = positions[position]
        return initial_position["moviment"]

    
    # Função que executa op CLI
    def prompt_commands(self, command: str = ""):

        match command: # Verifica o commando de entrada do prompt

            case "POSITION": # Situação que movimenta o braço a uma posição pré-definida no arquivo JSON
                jump_factor = 0 # Valor que define a elevação que do "pulo" do movimento jump
                counter = 0 

                for position in self.db["Positions"]: # Verifica a quantidade de posições existentes no arquivo JSON
                    print(f"Position name : {position["name"]} | Position code : {counter}")
                    counter += 1

                x,y,z,r,j1,j2,j3,j4 = self.device.pose() # Seta as posições atuais do braço em variáveis


                position = int(input("Position : ")) # Variável que recebe o index da posição que o robô ir
                to = self.open_data(position) # Variável que recebe todos os dados da posição

                if to["type"] == "j": # Verifica se o tipo da movimentação é do tipo jump
                    jump_factor = 50
                else :
                    jump_factor = 0

                if to["action"] == "on": # Verifica qual é o estado do ferramenta acoplada
                    self.device.suck(True)
                    self.device.move_to(x,y,z+jump_factor,r, True)
                    self.device.wait(250)
                    self.device.move_to(to["x"], to["y"], to["z"], to["r"])

                else:
                    self.device.suck(False)
                    self.device.move_to(x,y,z+jump_factor,r, True)
                    self.device.wait(250)
                    self.device.move_to(to["x"], to["y"], to["z"], to["r"])
                
            case "MOVE": # Situação que movimenta o braço para uma prosição qualquer
                try:
                    x = float(input("x : "))
                    y = float(input("y : "))
                    z = float(input("z : "))
                    r = float(input("r : "))
                except ValueError:
                    # Se alguns dos valores forem inválidos, os eixos são setados para os da posição inicial
                    x = 243
                    y = 0  
                    z = 151
                    r = 0
                self.device.move_to(x, y, z, r)

            case "ADD POSITION": # Sitauação que permite adicionar um ponto por linha de comando
                x = input("x : ")
                y = input("y : ")
                z = input("z : ")
                r = input("r : ")
                j1 = input("j1 : ")
                j2 = input("j2 : ")
                j3 = input("j3 : ")
                j4 = input("j4 : ")
                name = input("Name : ") # Nome da Posição
                t = input("Type :") # Tipo da movimentação
                action = input("Tool status : ") # Status da ferramenta
                self.add_position(x, y, z, r, j1, j2, j3, j4, name)# Função que realiza o salvamento da posição

            case "SAVE POSITION": # Situação que salva a posição do braço em que ele está parado
                name = str(input("\nName : ")) # Nome da posição 
                t = str(input("Type : ")).lower() # Tipo da movimentação
                action = str(input("Input : ")).lower() # Status da ferramenta
                self.save_actual_position(name, t, action) # Função que realiza o salvamento da posição

            case "TOOL": # Situação que muda o estado da ferramenta acoplada
                status = str(input("on/off : ")).lower() # Variável de entrada

                match status: # Verifica a entrada
                    case "on":
                        self.device.suck(True)
                    case "off":
                        self.device.suck(False)

            case "RESTART": # Situação que reinicia o programa
                python = sys.executable
                os.execl(python, python, *sys.argv)

            case "EXIT": # Situação que finaliza o prorama
                self.device.suck(False)
                self.device.close()
                exit()

        self.prompt_commands(input("\nCommand : ").upper()) # Recursividade da função do CLI


    # Função que adiciona um ponto ao JSON 
    def add_position(self, x:str , y:str , z:str , r:str , j1:str , j2:str , j3:str , j4:str , name: str, type:str, action:str):
        
        # transforma as entradas em tipo flaot
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            r = float(r)
            j1 = float(j1)
            j2 = float(j2)
            j3 = float(j3)
            j4 = float(j4)
        except ValueError:
            # Se nenhum dos valores for válido, todos serão igual a zero
            x = y = z = r = j1 = j2 = j3 = j4 = 0
            
        new_position = { # Dicionário que recebe os valores que serão adicionados ao arquivo JSON
            "name": name,
            "moviment": {
                "x": x,
                "y": y,
                "z": z,
                "r": r,
                "j1": j1,
                "j2": j2,
                "j3": j3,
                "j4": j4,
                "type" : type,
                "action" : action
            }
        }


    # Função que salva a posição atual do robô 
    def save_actual_position(self, name:str, type:str, action:str):
        x,y,z,r,j1,j2,j3,j4 = self.device.pose() # Armazena a psoição atual do robô em variáveis

        new_position = { # Dicionário que recebe os valores que serão adicionados ao arquivo JSON
            "name": name,
            "moviment": {
                "x": x,
                "y": y,
                "z": z,
                "r": r,
                "j1": j1,
                "j2": j2,
                "j3": j3,
                "j4": j4,
                "type" : type,
                "action" : action
            }
        }

        # Função que escreve a posição no arquivo JSON
        self.write_position_on_json(new_position)
        

    def write_position_on_json(self, position:dict):
        self.db["Positions"].append(position)

        # Abre o arquivo no mode de escrtia para fazer o update do elemento "Positions"
        with open(self.data_file_path, "w") as data_file:
            json.dump(self.db, data_file, indent=4)


BOBO = CardioBot() # Intancia a classe do braço robôtico

BOBO.connect_arm() # Conecta o braço ao computador