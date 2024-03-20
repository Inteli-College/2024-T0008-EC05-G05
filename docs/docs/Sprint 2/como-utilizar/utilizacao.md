---
title: Como utilizar a solução
sidebar_position: 2
---

## Interface de Comando

Na segunda sprint foi feito a Command Line Interface (CLI), que é uma interface que permite enviar comandos específicos ao robô e receber feedback imediato. Para realizar essa etapa, siga as instruções abaixo:

**Primeiro Passo: Instalar bibliotecas externas**

Os seguintes comandos irão instalar as dependências necessárias para rodar o projeto.
```
pip install inquirer
```
```
pip install yaspin
```

**Segundo Passo: Executar o arquivo**

```
python3 main.py
```

**Terceiro Passo: Escolher o commando a ser executado pelo braço robótico**

No terminal aparecerão algumas escolhas de comando para se dar ao robô, dentre elas:

- Connect Arm --> conecta o braço robótico;
- Home --> retorna o robô à posição inicial;
- Actual Position --> retorna as coordenadas atuais do braço juntamente com sua informações de juntas;
- Move Linear --> move o braço de forma linear, é preciso passar as coordenadas x, y, z, r;
- Move Join --> move o braço pelas juntas, é preciso passar as coordenadas x, y, z, r;
- Tougle Tool Status --> muda o status da ferramenta, sendo preciso passar qual ferramenta está send utilizada pelo robô;
- Disconnect Arm --> desconecta o braço;
- Exit Program --> fecha o programa;