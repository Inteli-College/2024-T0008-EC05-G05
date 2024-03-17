---
title: Sensor Ultrassônico
sidebar_position: 3
---

## Introdução
Em nossa solução, o objetivo da utilização do sensor ultrassônico é adicionar um processo de segurança para garantir que o robô pegou os itens antes que ele tente soltar o item no kit.

O código pode ser encontrado em : 

```
src\WebToRobot\CodigoRasp
```

## Bibliotecas utilizadas
- network
- urequests
- time
- machine
- utime

## Principais funções

- ultraS
Verifica a distância e com base nisso envia o dado de pegou em true ou false
- loop
Checa a conexão Wi-Fi

## Condições de funcionamento

- Conexão Wi-Fi
Nosso microcontrolador se conecta com a internet usando apenas seu nome e senha, com isso caso seja necessário realizar alguma outra ação como na internet IOT da inteli pode ocorrer algum conflito

## Conclusão