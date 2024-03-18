---
title: Visão Computacional
sidebar_position: 2
---

## Introdução

Visando a rastreabilidade dos medicamentos no nosso projeto, decidimos incrementar nessa sprint a visão computacional no nosso projeto.
Nossa aplicação consiste na utilização de uma câmera acoplada ao robô, que será capaz de fotografar os medicamentos e mandar a imagem para nosso servidor backend, que utiliza a biblioteca [QReader](https://pypi.org/project/qreader/), identificando assim o qrcode na imagem e realizando a leitura dos dados nele cintidos, salvando também a data e a hora em que aquele medicamento foi fotografado também. Dessa forma, é possível diferenciar em qual kit cada medicamento está, garantindo asism a rastreablidade dos itens.

O código pode ser encontrado em `src\WebToRobot\app.py`, na função assíncrona "*capturar_qr_code*".


## Montagem

Para utilizar a câmera, basta utilizar o cabo USB da mesma e conectá-la ao pc.

## Principais funções

- Guarda os dados de cada qrcode lido no banco de dados
- Permite a rastrebalidade por meio da fata e hora salvas.

## Conclusão

Dessa forma, com essa funcionalidade em vigor, fortalecemos a segurança e a confiabilidade do nosso sistema, garantindo que cada medicamento seja monitorado de forma precisa e eficiente. Além disso, ao armazenar os dados no banco de dados, criamos um registro detalhado que pode ser consultado posteriormente, contribuindo para a transparência e a prestação de contas em relação ao manuseio e distribuição dos medicamentos.

Ainda pensando em melhorar a segurança, implementamos o uso do sensor ultrassônico, que será explicado na seção a seguir. 