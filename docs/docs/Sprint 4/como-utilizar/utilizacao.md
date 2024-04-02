---
title: Como utilizar a solução
sidebar_position: 3
---
Durante esta sprint, foram desenvolvidos com grande ênfase a integração da API do robô e o frontend. No backend também houve a alteração do banco de dados de TinyDB para SQLITE3.
Para executar a solução completa, siga os passos abaixo.


## Frontend 

O frontend foi desenvolvido em react e para ser executando no ambiente de desenvolvimento, os passos são bem simples. 

**Primeiro Passo: Acessar a pasta raiz do frontend**

```bash
cd src/frontend
```

**Segundo Passo: Instalar o pacote npm**

Os seguintes comandos irão instalar as dependências necessárias para rodar o projeto.

```bash
npm install
```

**Terceiro Passo: Executar o frontend**

```bash
npm start
```

Pronto, agora o frontend já está funcionando e aguardando a conexão com o backend para ficar totalmente funcional. 

## Backend 

O backend desenvolvido ao longo desta sprint tem como objetivo permitir a alteração dinâmica de cinco kits e tornar o frontend totalmente dinâmico. 

**Primeiro Passo: Criar e ativar o ambiente virtual**

```bash
cd src/backend/api | python -m venv venv
```

``` bash
venv\scripts\activate
```

**Segundo Passo: Instalar todas dependências**

É muito importante se atentar e entrar na pasta raíz da API.

```bash
cd src/backend/api
```

```bash
pip install -r requirements.txt
```

**Terceiro Passo: Iniciar o servidor**

Entrar na pasta que está localizada a API. 

```bash
cd src/backend/api/warehouse
```

Iniciar o servidor 

```bash
uvicorn warehouse:app --reload
```

Entrar na pasta que está localizada a API. 

```bash
cd src/backend/api/dashboard
```

Iniciar o servidor 

```bash
uvicorn dashboard_api:app --reload
```

## API de comunicação com o robô

A API de comunicação com o robô foi desenvolvida em Python e utiliza a biblioteca `FastAPI` e nos possibilita controlar o robô através de endpoints. Para executar a API, siga os passos abaixo.

**Primeiro Passo: Acessar a pasta raiz da API**

```bash
cd src/backend/api/WebToRobot
```

**Segundo Passo: Criar e ativar o ambiente virtual**

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

**Terceiro Passo: Instalar todas dependências**

```bash
pip install -r requirements.txt
```

**Quarto Passo: Iniciar o servidor**

Iniciar o servidor 

```bash
uvicorn app:app --host 0.0.0.0 --reload --port 80
```

Estamos rodando essa API como host 0.0.0.0 porque queremos que ela seja acessível de qualquer lugar na rede local, inclusive com o nosso Raspberry Pico. Então para a comunicar com a API, basta acessar o endereço `http://<ip_do_computador>:80/docs`.


## Código do Raspberry Pico (Sensor Ultrassônico)

O código do Raspberry Pico foi desenvolvido em python através do MicroPython. Para executar o código, siga os passos abaixo.

**Primeiro Passo: Acessar a pasta raiz do código**

```bash
src/WebToRobot/CodigoRasp
```

**Segundo Passo: Conectar o Raspberry Pico ao computador**

Conectar o Raspberry Pico ao computador e copiar o código para o ficheiro interno dele ou dentro do software Thonny.


**Terceiro Passo: Monte o circuito eletrônico do Raspberry Pico**

Monte o circuito baseado no diagrama de montagem, que pode ser encontrado aqui.

**Quarto Passo: Executar o código**

Executar o código no Raspberry Pico. 


Após seguir todos os passos, a solução estará pronta para ser utilizada.
