---
title: Estrutura de pastas
sidebar_position: 1
---

Antes de tudo, é importante entender como está funcionando a estrutura de pastas e a modularização do código.

Dentro do nosso [repositório do GitHub](https://github.com/Inteli-College/2024-T0008-EC05-G05), temos as seguintes pastas:

```
.
├── .github/workflows
├── docs
├── media
└── src
--.gitignore
--README.md
--package-lock.json
```
Para explicar apenas o código-fonte especificamente, vamos selecionar a pasta "src":

```
src
└── modules
    --init.py
    --arm.py
    --file_menager.py
    --kit_menager.py
├── venv
--data.json
--dobot.py
--main.py
--requirements.txt
--test.py

```

Na pasta *modules*, estão os arquivos (módulos) que contém as classes que são rodadas no arquivo *main*, que está fora da pasta. 

- *arm.py:* arquivo onde está a classe que controla o braço robótico;
- *file_menager.py:* arquivo onde está a classe que gerencia os arquivos json, nos quais os dados dos itens são salvos;
- *kit_menager.py:* por enquanto ainda não faz nada, mas futuramente terá a classe que gerencia as informações dos kits.

Os arquivos JSON mencionados são uma estrutura de banco de dados que está sendo criado na pasta "src", onde são salvas as posições, kits e itens.

> As posições tem seus nomes de identificação, coordenadas e o tipo de movimento (moveL ou moveJ);

> Os itens tem seus nomes e suas posições, na qual é umas das posições já salvas;

> Já os kits, embora sua classe ainda não esteja finalizada, terão seus respectivos nomes, além dos itens e suas quantidades.

> Outra coisa a ser adicionada na próxima Sprint é o datetime log dos dados salvos, isso para cada item, posição e kit, ou seja, salvar quando cada dado foi criado.