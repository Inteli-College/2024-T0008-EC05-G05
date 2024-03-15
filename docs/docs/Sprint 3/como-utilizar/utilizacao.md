---
title: Como utilizar a solução
sidebar_position: 3
---
Durante esta sprint, foram desenvolvidos com grande ênfase uma API capaz de se conectar ao robô e enviar requisições para o mesmo, um frontend com o início de algumas integrações, um backend com rotas já funcionais, e um banco de dados feito utilizando o TinyDB. Para executar a solução completa, siga os passos abaixo.


## Frontend 

O frontend foi desenvolvido em react e para ser executando no ambiente de desenvolvimento, os passos são bem simples. 

**Primeiro Passo: Acessar a pasta raiz do frontend**

```
cd src/frontend/cardiobot
```

**Segundo Passo: Instalar o pacote npm**

Os seguintes comandos irão instalar as dependências necessárias para rodar o projeto.

```
npm install
```

**Terceiro Passo: Executar o frontend**

```
npm start
```

Pronto, agora o frontend já está funcionando e aguardando a conexão com o backend para ficar totalmente funcional. 

## Backend 

O backend desenvolvido ao longo desta sprint tem como objetivo permitir a alteração dinâmica de cinco kits e tornar o frontend totalmente dinâmico. 

**Primeiro Passo: Acessar a pasta raiz do backend**

```
cd src/api
```

**Segundo Passo: Criar e ativar o ambiente virtual**

```
python -m venv venv
```

```
cd venv/scripts
```

```
activate
```


**Terceiro Passo: Instalar todas dependências**

```
pip install -r requirements.txt
```

**Quarto Passo: Iniciar o servidor**

Entrar na pasta que está localizada a API. 

```
cd src\api\warehouse
```

Iniciar o servidor 

```
uvicorn warehouse:app --reload
```



