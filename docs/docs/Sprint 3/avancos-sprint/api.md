---
title: API do robô
sidebar_position: 5
---

O objetivo dessas APIs, criada em FastApi é permitir a comunicação com o braço robótico para controlar e monitorar as operações dele atráves requisições. Além disso, essas APIs fazem a integração do nosso sistema com outros dispositivos como Raspberry Pi Pico e câmeras para leitura de QR Codes.

A API oferece diversos endpoints que permitem executar ações como conectar ao robô, mover o robô para posições específicas, capturar e interpretar QR Codes, além de interagir com sensores para coleta de dados. 

Todo código da API está localizado na pasta `\2024-T0008-EC05-G05\src\WebToRobot`. Além disso, os dados dessa API está sendo armazenado em um banco de dados Tinydb, localizado na pasta `\2024-T0008-EC05-G05\src\WebToRobot\db.json`. O banco de dados contem a seguinte estrutura:

####  Tabelas:
1. **Itens**: Armazena informações sobre os itens individuais.
2. **Kits**: Contém informações sobre os kits, que são conjuntos de itens.
3. **Positions**: Registra posições específicas para movimentação do robô Dobot.

#### Estrutura da Tabela `Itens`
- **item_code**: Código identificador único do item (String).
- **name**: Nome do item (String).
- **initial_position**: Código da posição inicial do item (String).
- **final_position**: Código da posição final do item (String).

#### Estrutura da Tabela `Kits`
- **kit_code**: Código identificador único do kit (String).
- **name**: Nome do kit (String).
- **items**: Lista de códigos de itens que compõem o kit (Lista de Strings).

#### Estrutura da Tabela `Positions`
- **position_code**: Código identificador único da posição (String).
- **x**: Coordenada X para a posição (Número).
- **y**: Coordenada Y para a posição (Número).
- **z**: Coordenada Z para a posição (Número).
- **r**: Coordenada R (rotação) para a posição (Número).

É importante também entender como o robô é controlado. Nos criamos uma classe que contem todos os comandos espeficos de controle do braço robotico, através da biblioteca `pydobot`. A classe chamada Dobot está localizada no arquivo `dobot.py` e é responsável por controlar o braço robótico.

A seguir vamos detalhar cada endpoint, incluindo seu propósito, método HTTP, parâmetros necessários e o formato das respostas.

#### 1. Conectar ao Dobot
- **Endpoint**: `/conectar_dobot/`
- **Método**: GET
- **Parâmetro**: `porta` (string)
- **Descrição**: Tenta conectar o robô Dobot a uma porta do computador especificada. Retorna uma mensagem de sucesso ou erro.

#### 2. Mover para Posições
- **Endpoint**: `/mover_para_posicoes/`
- **Método**: GET
- **Parâmetros**: `posicao_inicial` (string), `posicao_final` (string)
- **Descrição**: Move o Dobot para as posições inicial e final especificadas. Entre o movimento incial e final, existe movimentos para posições de segurança, onde é feito a verificação se foi pego algum item atráves do sensor ultrassônico e a leitura de QR Code.

#### 3. Capturar QR Code
- **Endpoint**: `/capturar`
- **Método**: GET
- **Descrição**: Captura e decodifica um QR Code usando uma câmera conectada, retornando os dados decodificados.

#### 4. Receber Dados do Raspberry Pi Pico
- **Endpoint**: `/pico_data`
- **Método**: POST
- **Corpo da Requisição**: `PicoData` (BaseModel de JSON com a chave "pegou" com valor booleano)
- **Descrição**: Recebe dados do Raspberry Pi Pico, armazena-os e retorna uma confirmação de recebimento.

#### 5. Obter Dados Recebidos do Pico
- **Endpoint**: `/pico_data`
- **Método**: GET
- **Descrição**: Retorna os últimos dados recebidos do Raspberry Pi Pico.

#### 6. Montar Kit
- **Endpoint**: `/montar_kit/`
- **Método**: GET
- **Parâmetro**: `kit_code` (string)
- **Descrição**: Monta um kit baseado no código do KIT fornecido, utilizando o Dobot para mover os itens necessários.

#### 7. Salvar Posição
- **Endpoint**: `/salvar_posicao/`
- **Método**: GET
- **Parâmetros**: `position_code` (string)
- **Descrição**: Salva ou atualiza a posição atual do Dobot com o código de posição fornecido.


Para rodar a API, é necessário instalar as dependências do projeto. Para isso, basta executar o comando `pip install -r requirements.txt` na pasta `\2024-T0008-EC05-G05\src\WebToRobot`. Após a instalação, execute o comando `uvicorn app:app --host 0.0.0.0 --reload --port 80` para iniciar o servidor. Estamos rodando essa API como host 0.0.0.0 porque queremos que ela seja acessível de qualquer lugar na rede local, inclusive com o nosso Raspberry Pico. Então para a comunicar com a API, basta acessar o endereço `http://<ip_do_computador>:80/docs`.

