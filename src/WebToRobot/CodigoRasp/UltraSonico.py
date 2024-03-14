import network
import urequests
import time
from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

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
        urequests.post('http://10.128.0.8/pico_data', json={"pegou": "True"})
    else:
        print("Não pegou")
        urequests.post('http://10.128.0.8/pico_data', json={"pegou": "False"})
        print("dado enviado")

                
def loop():
    if wlan.isconnected():  # Check if still connected to Wi-Fi
        try:
            check = urequests.get('http://10.128.0.8/check')
            
            # Diagnóstico
            print(repr(check.text))  # Mostra a representação da string
            print("Tamanho da string recebida:", len(check.text))
            
            # Limpeza e comparação
            clean_text = check.text.strip()
            if clean_text == '"Ativar"':
                print("Entrou aqui")
                ultraS()
            else:
                print("Não entrou no if do ativar", "|", clean_text, "|")
                
        except OSError as e:
            print("Network error:", e)
    else:
        print("Not connected to Wi-Fi.")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Inteli.Iot', '@Intelix10T#')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

meu_ip = wlan.ifconfig()[0]
print(f"IP:{meu_ip}")

while True:
   loop()
   utime.sleep(1)
