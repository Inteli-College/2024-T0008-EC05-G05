# Importação de bibliotecas necessárias
import network  # Para configurar a rede Wi-Fi
import urequests  # Para fazer solicitações HTTP
import time  # Para manipulação de tempo
from machine import Pin  # Para controle de pinos do dispositivo
import utime  # Para manipulação de tempo em MicroPython

# Configuração dos pinos do sensor ultrassônico
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

ip_servidor = "10.128.0.8"

# Função para medir a distância usando o sensor ultrassônico
def ultraS():
    print("Entrou no UltraS")
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ", distance, "cm")
    if distance < 15:
        print("Pegou sim, ta safe")
        urequests.post(f'http://{ip_servidor}/pico_data', json={"pegou": "True"})
    else:
        print("Não pegou")
        urequests.post(f'http://{ip_servidor}/pico_data', json={"pegou": "False"})
        print("dado enviado")

# Função principal para executar o loop
def loop():
    if wlan.isconnected():  # Verificar se ainda está conectado ao Wi-Fi
        try:
            check = urequests.get('http://{ip_servidor}/check')
            print(repr(check.text)) 
            print("Tamanho da string recebida:", len(check.text))
            clean_text = check.text.strip()
            if clean_text == '"Ativar"':
                print("Entrou aqui")
                ultraS()
            else:
                print("Não entrou no if do ativar", "|", clean_text, "|")
                
        except OSError as e:
            print("Network error:", e)
    else:
        print("Não conectado ao Wi-Fi.")

# Configuração da conexão Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Inteli.Iot', '@Intelix10T#')

# Aguardando a conexão ser estabelecida
while not wlan.isconnected() and wlan.status() >= 0:
    print("Aguardando conexão:")
    time.sleep(1)

# Obtendo o endereço IP do dispositivo
meu_ip = wlan.ifconfig()[0]
print(f"IP:{meu_ip}")

# Loop principal
while True:
#    loop()
   ultraS()
   utime.sleep(1)
