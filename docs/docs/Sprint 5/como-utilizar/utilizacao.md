---
title: Como utilizar a solução
sidebar_position: 3
---

Aqui você encontrará um guia de como utilizar a solução desenvolvida pelo grupo.

## Raspberry Pico (Sensor de Distância)

Para utilizar o sensor de distância, siga os passos abaixo:

**Primeiro Passo: Montar o circuito do Raspberry Pico**

A seguir é apresentado o esquema elétrico do circuito do Raspberry Pico:

<div align="center"> 

**Esquema elétrico dos periféricos** 

![Esquema elétrico dos periféricos](/../static/img/esquema-circuito/circuito-elétrico.jpg)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

**Segundo Passo: Instalar o firmware no Raspberry Pico**

Para instalar o firmware no Raspberry Pico, siga os passos abaixo:

1. Instale o [Thonny IDE](https://thonny.org/).
2. Faça o setup inicial do Raspberry Pico, seguindo o [tutorial oficial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).
3. Instale o [MicroPython](https://micropython.org/download/rp2-pico/).
4. Abra o Thonny IDE e conecte o Raspberry Pico ao computador.
5. Vá até a pasta `src/CodigoRasp/UltraSonico.py` e copie o código.
6. Cole o código no Thonny IDE, em um arquivo chamdado `main.py` e substitua os valores de `SSID` e `PASSWORD` pelas credenciais da sua rede Wi-Fi e o valor de `ip_servidor` pelo IPV4 do seu computador.
7. Clqiue em `Run` para executar o código.

Nos estamos utilizando o MicroPython para programar o Raspberry Pico.

Após seguir todos os passos, o sensor de distância estará pronto para ser utilizado e pode ser ligado utilizando alguma fonte de energia, como um power bank.


## Frontend e Backend

Para utilizar o frontend e o backend, siga os passos abaixo:

1. Vá no diretorio raiz do projeto e execute o comando `python main.py`.
    1.1 Caso você não tenha o Python instalado, você pode baixar o executável [aqui](https://www.python.org/downloads/).
    1.2 Esse comando vai iniciar 3 terminais, um para o frontend, um para o backend e um para o servidor de comunicação com o Raspberry Pico e robô.
2. Vá até o arquivo `src/frontend/src/components/kit_description_popup/KitDescriptionPopup.js` e substitua o valor de `ip_servidor` pelo IPV4 do seu computador.
    2.1 Isso vai fazer com que o frontend consiga se comunicar com o backend do robô e com o Raspberry Pico.
3. Abra o navegador e acesse o endereço `http://localhost:3000/`.

Após seguir todos os passos, a solução estará pronta para ser utilizada.




