# Importação de bibliotecas necessárias
import network  # Para configurar a rede Wi-Fi
import urequests  # Para fazer solicitações HTTP
import time  # Para manipulação de tempo
from machine import Pin  # Para controle de pinos do dispositivo
import utime  # Para manipulação de tempo em MicroPython
import gc  # garbage collection module

gc.enable()

# Configuração dos pinos do sensor ultrassônico
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


ip_servidor = "10.128.0.37:8800"

# Função para medir a distância usando o sensor ultrassônico
def ultraS():
    gc.collect()
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
    print("Distancia do objeto ", distance, "cm")

    payload = {"pegou": "True" if distance < 15 else "False"}
    try:
        urequests.post(f'http://{ip_servidor}/pico_data', json=payload)
        print("Dado enviado")
    except OSError as e:
        print("Network error:", e)
    finally:
        gc.collect()  # Limpar a memoria antes de fazer a requisição

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
   ultraS()
   utime.sleep(1)
