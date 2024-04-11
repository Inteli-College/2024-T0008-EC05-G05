---
title: Backend
sidebar_position: 2
---

## Introdução

Nesta seção, você pode conferir a versão final do projeto e acompanhar as mudanças, bem como entender o funcionamento do backend.

O backend consiste em duas APIs desenvolvidas em Python utilizando o framework FastAPI. A escolha deste framework foi motivada pela sua capacidade de realizar requisições assíncronas e pela extensa documentação disponível, o que facilita o desenvolvimento e a manutenção do código.

Para acessar as APIs, basta navegar até a pasta src/backend/api, onde estão localizados os arquivos WebToRobot.py e Stock.py. Cada API possui uma função específica, detalhada ao longo desta documentação. Recomenda-se também explorar a seção de Arquitetura da Solução para obter uma visão macro do projeto.

## API WebToRobot 
Esta API é responável por realizar a comunicação do front-end com o braço robôtico, permitindo a execução dos comandos com os elementos da aplicação web.

Vale ressaltar que esse API está dividida em algumas paretes:
- Conexão com o robô;
- Movimentação do robô;
- Registros de ações;

### Rotas da API

#### Conexão com o robô

Nessa área, estão as rotas de conexão com o braço robótico:

- /conectar_dobot/  ~>  Faz a conexão automática com o braço, caso ele esteja conectado à uma porta do computador;
- /conectar_dobot_porta/ ~> Concta o robô com o cpmputador, com uma porta específica, passada na hora da conexão;

<div align="center">

**Imgem 1:** Rotas de conexão com o braço robótico

![imagem](../../../static/img/apis/conectart-robo.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>

#### Movimentação

Aqui, é a rota de movimentação do braço para a posição salva dos itens.

<div align="center">

**Imgem 2:** Parte 1 :  Rota de movimentação do braço robótico

![imagem](../../../static/img/apis/mover-posicao-1.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>

<div align="center">

**Imgem 3:** Parte 2 :  Rota de movimentação do braço robótico

![imagem](../../../static/img/apis/mover-posicao-2.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>

#### Leitura QRCode

Nessa parte do códiga, é onde está a rota de leitura do QRCode do produto.

Ela permite o salvamento dos dados daquele item em um arquivo JSON `src/backend/api/dados_qr.json`, que registra informações que são:
- Data e hora da leitura do código QR;
- Informações do código QR;

<div align="center">

**Imgem 4:**  Rota de leitura do QRCode

![imagem](../../../static/img/apis/capturar-qrcode.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>


#### Conexão com sensor ultrassônico

Essa rota é responsável por conectar com o sensor ultrassônico e verificar se o item pego pelo braço, de fato foi pego.

<div align="center">

**Imgem 5:** Rota leitura de dados do sensor

![imagem](../../../static/img/apis/detectar-item.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>


#### Montar Kit

Aqui é realizada a montatem do kits. Esse comando é enviado pelo front.


<div align="center">

**Imgem 6:** Rota de montagem dos kits

![imagem](../../../static/img/apis/montar-kit.png)

**Fonte:** Desenvolvido pelo grupo Cardio-Bot
</div>


## API Stock

A API do estoque é a responsável por todas as interações com o frontend. A ideia por trás dessa API é permitir a interação do frontend, sistema de logs e banco de dados.


#### Rotas da API

O código da API está dividido em três partes principais, cada um tem sua função única. 

##### Interação com o Dashboard

Esta parte da API fornece os logs para a tela do dashboard. Os logs são solicitados com base no período selecionado no dropdown, abrangendo itens individuais de cada kit, kits específicos e interações com o robô.

O código correspondente pode ser visualizado na imagem abaixo:

![logs](../../../static/img/apis/logsd.png)

##### Interação com os kits 

A lógica pensada no desenvolvimento dos kits foi a de criar cinco kits padrões. A partir disso, o usuário pode atualizar a composição de cada um desses kits interagindo com os mesmos na tela de supplies. 

Na imagem abaixo é possível ver a rota de update.

![kits](../../../static/img/apis/stock-update.png)

##### Logs das alterações 

Manter a rastreabilidade é uma das funções mais importantes do projeto. Assim, foi desenvolvido um sistema de logs que mostra quem atualizou determinado kit, hora da alteração e qual kit foi modificado. 

É possível conferir o código na imagem abaixo. 

![write logs](../../../static/img/apis/log-create.png)



## Conclusão

Durante o desenvolvimento do backend, optamos por uma solução que permitisse o desacoplamento das partes e sistemas, evitando monolitos. O objetivo foi desenvolver duas APIs distintas: uma para comunicação com o robô e outra para interação com o frontend.

