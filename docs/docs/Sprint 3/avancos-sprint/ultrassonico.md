---
title: Sensor Ultrassônico
sidebar_position: 3
---

## Introdução

Nessa solução o objetivo da utilização do sensor ultrassônico é adicionar um processo de segurança para garantir que o robô pegou os itens antes que ele tente soltar o item no kit.

O código pode ser encontrado em : 

```
src\WebToRobot\CodigoRasp
```

## Montagem

Nessa seção será abordada os componentes e a forma de montagem para o funcionamento do sensor. Os componentes que estão sendo usados são: uma raspberry pi pico W, um sensor ultrassônico HC-SR04 e 4 cabos para ligar o sensor ao microcontrolador. Primeiramente, conecta-se o GND e o VCC do sensor ao GND (pino 23) e o 3v3 (pino 38), respectivamente, da raspberry pi pico W. Após isso, conecte o Echo e o Trig do sensor nos pinos 4 e 5 (GP2 e GP3) do microcontrolador.

É possível visualizar a pinagem no esquema a seguir, que também inclui a câmera:

<div align="center"> 

**Esquema elétrico dos periféricos** 

![Esquema elétrico dos periféricos](/../static/img/esquema-circuito/circuito-elétrico.jpg)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>




## Bibliotecas utilizadas

- network
- urequests
- time
- machine
- utime

## Principais funções

- ultraS
Verifica a distância e com base nisso envia o dado de pegou em True ou False
- loop
Verifica se está conectado ao Wifi. Caso esteja, manda uma requisição para o servidor para saber se pode chamar a função ultraS.

## Condições de funcionamento

- Conexão Wi-Fi
Nosso microcontrolador se conecta com a internet usando apenas seu nome e senha, com isso caso seja necessário realizar alguma outra ação para conectar, como logar com o e-mail ou qualquer tipo de verificação adicional. Além disso, o computador que estiver usando a solução deve estar conectado a mesma internet que o microcontrolador.

## Conclusão

A integração do sensor oferece uma camada de segurança vital ao processo do robô, garantindo que só libere os itens no kit após confirmar sua captura. Com a Raspberry Pi Pico W e o sensor de distância, o sistema monitora a proximidade dos objetos com precisão, tomando decisões com base nesses dados. Assim, essa solução proporciona uma forma confiável e eficaz de garantir a integridade das operações do robô, promovendo segurança e eficiência.
