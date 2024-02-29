import pydobot, math
from time import sleep, time
from yaspin import yaspin
from .file_menager import DataMenager
from serial.tools import list_ports


class CardioBot(DataMenager):
    def __init__(self, db_path) -> None:
        super().__init__(db_path)
        self.loader = yaspin()
        self.connection_status = False
        self.loop = True
        self.tool_status = None
        self.attemptions = 1

    
    def timer(self, seconds):
        seconds = seconds
        start_time = time()

        while True:
            elapsed_time = time() - start_time
            remaining_time = max(0, seconds - elapsed_time)

            remaining_time = math.trunc(remaining_time)

            print(f"Conecte o dispositivo: {remaining_time} segundos", end='\r')

            if elapsed_time >= seconds:
                break


    def connect(self):
        print("\nConectando Robô")
        self.loader.start()
        sleep(1)
        if(self.attemptions <= 2):
            try:
                available_ports = list_ports.comports() # Verifica as portas do computador
                port = available_ports[0].device # Seta a porta disponível
                self.device = pydobot.Dobot(port=port, verbose=False)
                self.connection_status = True # Conecta ao braço à porta
                self.loader.ok("✅ Robô conectado\n")
            except:
                self.loader.fail(f"\n\n💥 Não foi possível achar dispositívos conectados.\nTentativa:{self.attemptions}\n")

                self.timer(20)

                self.attemptions += 1
                sleep(2)
                self.connect()

            sleep(1.5)
        else:
            self.loader.fail("☠︎︎ Ecesso de tentativas. O programa será parado\n")
            sleep(1.5)
            exit()
        


    def disconnect(self):
        print("\nDesconectando Robô\n")
        self.loader.start()
        sleep(0.25)
        
        try:
            self.device.suck(False)
            self.device.move_to(243, 0, 150, 0, True)
            self.device.close()
            self.loader.ok("✅ Robô desconectado\n")
        except:
            self.loader.fail("💥 Nenhum robô encontrado\n")

        sleep(1.25)


    def move(self, cordenates:dict, jump_factor:float):
        print("Iniciando movimentação")
        self.loader.start()
        sleep(1)
        try:
            actual_position = self.get_position()
            if jump_factor and actual_position["z"]+jump_factor <= 135:
                self.device.move_to(actual_position["x"], actual_position["y"], actual_position["z"]+jump_factor, actual_position["r"], True)

            self.device.move_to(cordenates["x"], cordenates["y"], cordenates["z"]+jump_factor, cordenates["r"], True)
            self.device.move_to(cordenates["x"], cordenates["y"], cordenates["z"], cordenates["r"], True)
            self.loader.ok("✅ Movimentação concluída\n")
        except:
            self.loader.fail("💥 Braço desconecato\n")
            sleep(1.25)
            self.connect()


    
    def get_position(self):
        print("Pegando posições")
        self.loader.start()
        sleep(1)


        try:
            x,y,z,r,j1,j2,j3,j4 = self.device.pose()
        except:
            self.loader.fail("💥 Braço desconectado")
            sleep(1.25)

            self.connect()

        x,y,z,r,j1,j2,j3,j4 = self.device.pose() 
        
        saved_position = {
            "x" : x,
            "y" : y,
            "z" : z,
            "r" : r,
            "j1" : j1,
            "j2" : j2,
            "j3" : j3,
            "j4" : j4,
        }

        sleep(1)

        return saved_position

    