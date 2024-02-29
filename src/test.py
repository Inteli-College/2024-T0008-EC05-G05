from serial.tools import list_ports
import pydobot, json


class CardioBot:
    def __init__(self) -> None:
        self.data_file_path = "src/data.json" # Caminho do arquivo JSON
        with open(self.data_file_path, "r") as data_file:  # Abre o arquivo em binário
            self.db = json.load(data_file)


    # Conecta o computador ao braço robótico
    def connect_arm(self):
        available_ports = list_ports.comports() # Verifica as portas do computador
        port = available_ports[0].device # Seta a porta disponível
        self.device = pydobot.Dobot(port=port, verbose=False) # Conecta ao braço à porta 
        self.prompt_commands(input("Commando : ").upper()) # Inicia os comandos po CLI


    # Acessa os daos de posições do arquivo JSON
    def open_positions_data(self, p: int):
        positions = self.db["Positions"]
        position = positions[p]
        return position["movement"] # Retorna os valores da posição


    def open_kits_data(self):
        kits = self.db["Kits"]
        counter = 0
        for i in kits:
            print(f"\nKit name : {i["name"]} | Kit code : {counter}")
            counter += 1

        kit_code = int(input("\nWrite the kit code : "))
        kit_itens = kits[kit_code]["itens"]
        kit_item_quant = kits[kit_code]["quant"]

        self.access_itens_infos(kit_itens, kit_item_quant)

    
    def access_itens_infos(self, itens_list:list, quant:list):
        itens = self.db["Itens"]

        # for i in itens_list:
        #     print(f"Item : {itens[i]["name"]} --> Quant : {quant[i]}")

        for i in itens_list:
            print(f"{itens[i]["name"]}")

    
    # Função que executa op CLI
    def prompt_commands(self, command: str = ""):

        with open(self.data_file_path, "r") as data_file:  # Abre o arquivo em binário
            self.db = json.load(data_file)

        match command: # Verifica o commando de entrada do prompt

            case "POSITION": # Situação que movementa o braço a uma posição pré-definida no arquivo JSON
                counter = 0 

                for position in self.db["Positions"]: # Verifica a quantidade de posições existentes no arquivo JSON
                    print(f"\n\nPosition name : {position["name"]} | Position code : {counter}\n\n")
                    counter += 1

                x,y,z,r,j1,j2,j3,j4 = self.device.pose() # Seta as posições atuais do braço em variáveis

                position = int(input("Position : ")) # Variável que recebe o index da posição que o robô ir
                movement = self.open_positions_data(position) # Variável que recebe todos os dados da posição

                self.move_arm(movement["x"], movement["y"], movement["z"], movement["r"], movement["jump-factor"], movement["tool"])
            
            case "SERIAL":
                movements_list_input:str = str(input("movement indexs : "))
                movements_list_to_do:list = movements_list_input.split(" ")

                for movement in movements_list_to_do:
                    print(movement)
                    move = self.open_positions_data(int(movement))
                    self.move_arm(move["x"], move["y"], move["z"], move["r"], move["jump-factor"], move["tool"])

            case "KITS":
                self.open_kits_data()
                
            case "MOVE": # Situação que movementa o braço para uma prosição qualquer
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
                t = input("Type :") # Tipo da movementação
                action = input("Tool status : ") # Status da ferramenta
                self.add_position(x, y, z, r, j1, j2, j3, j4, name)# Função que realiza o salvamento da posição

            case "SAVE POSITION": # Situação que salva a posição do braço em que ele está parado
                name = str(input("\nName : ")) # Nome da posição 
                t = str(input("Jump Factor : ")).lower() # Tipo da movementação
                action = str(input("Toll Status : ")).lower() # Status da ferramenta
                self.save_actual_position(name, t, action) # Função que realiza o salvamento da posição

            case "CREATE KIT":
                name = str(input("\nKit name : "))
                itens_list = str(input("Itens IDs : ")).split(" ")
                itens_quant_list = str(input("Itens quantitie : ")).split(" ")

                # for i in :

                #     print(i)

                self.save_kit_preset(name, itens_list, itens_quant_list)


            case "TOOL": # Situação que muda o estado da ferramenta acoplada
                status = str(input("on/off : ")).lower() # Variável de entrada

                match status: # Verifica a entrada
                    case "on":
                        self.device.suck(True)
                    case "off":
                        self.device.suck(False)

            case "EXIT": # Situação que finaliza o prorama
                self.device.suck(False)
                self.device.move_to(243, 0, 150, 0, True)
                self.device.close()
                exit()

        self.prompt_commands(input("\nCommand : ").upper()) # Recursividade da função do CLI


    # Função que adiciona um ponto ao JSON 
    def add_position(self, x:str , y:str , z:str , r:str , j1:str , j2:str , j3:str , j4:str , name: str, jump:str, action:str):
        
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
            jump = float(jump)
        except ValueError:
            # Se nenhum dos valores for válido, todos serão igual a zero
            x = y = z = r = j1 = j2 = j3 = j4 = jump = 0
            
        new_position = { # Dicionário que recebe os valores que serão adicionados ao arquivo JSON
            "name": name,
            "movement": {
                "x": x,
                "y": y,
                "z": z,
                "r": r,
                "j1": j1,
                "j2": j2,
                "j3": j3,
                "j4": j4,
                "jump-factor" : jump,
                "tool" : action
            }
        }

        self.write_data_on_json(new_position, "Positions")

    # Função que salva a posição atual do robô 
    def save_actual_position(self, name:str, jump:str, action:str):
        x,y,z,r,j1,j2,j3,j4 = self.device.pose() # Armazena a psoição atual do robô em variáveis

        jump = float(jump)

        new_position = { # Dicionário que recebe os valores que serão adicionados ao arquivo JSON
            "name": name,
            "movement": {
                "x": x,
                "y": y,
                "z": z,
                "r": r,
                "j1": j1,
                "j2": j2,
                "j3": j3,
                "j4": j4,
                "jump-factor" : jump,
                "tool" : action
            }
        }

        # Função que escreve a posição no arquivo JSON
        self.write_data_on_json(new_position, "Positions")

    
    def move_arm(self, x:float, y:float, z:float, r:float, jump:float=0, tool:str="off"):
        x_,y_,z_,r_,j1_,j2_,j3_,j4_ = self.device.pose()

        self.device.move_to(x_,y_,z_+jump,r_, True)
        self.device.wait(250)
        self.device.move_to(x,y,z+jump,r, True)
        self.device.move_to(x,y,z,r, True)

        if tool == "on": # Verifica se o tipo da movementação é do tipo jump
            self.device.suck(True)
        else :
            self.device.suck(False)
     

    def write_data_on_json(self, json_data:dict, element:str):
        self.db[element].append(json_data)
        

        # Abre o arquivo no mode de escrtia para fazer o update do elemento 
        with open(self.data_file_path, "w") as data_file:
            json.dump(self.db, data_file, indent=4)

    
    def save_kit_preset(self, name:str, itens:list, quant:list):
        for i in range(len(itens)-1):
            int(itens[i], quant[i])

        new_kit = {
            "name"  : name,
            "itens" : itens,
            "quant" : quant
        }

        self.write_data_on_json(new_kit, "Kits")


    
class Mover(CardioBot):
    def __init__(self) -> None:
        super().__init__()


BOBO = CardioBot() # Intancia a classe do braço robôtico

BOBO.connect_arm() # Conecta o braço ao computador