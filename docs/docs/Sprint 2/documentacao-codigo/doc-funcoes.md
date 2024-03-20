---
title: Classes
sidebar_position: 2
---

Agora, vamos entender mais a fundo como está funcionando cada uma das classes citadas anteriormente:

## CardioBot

### Bibliotecas importadas:
 
 - pydobot;
 - math;
 - yaspin;
 - time (especificamente a função sleep);
 - serial.tools (especificamente a função list_ports);
 - Classe **DataMenager**, que é instanciada em outro arquivo.

Dentro do arquivo **arm.py**, está o código que implementa uma classe chamada CardioBot, que controla o braço robótico e descreve suas funções, dentre elas:

- **connect:** Conectar-se à porta serial;
- **disconnect:** Desconectar-se à porta serial;
- **move:** Mover-se de acordo com as coordenadas e o tipo de movimento (linear ou usando as juntas);
- **get_position:** Retornar as coordenadas da posição atual;
- Além disso, todas as funções contém timers que regulam a velocidade das ações citadas.

## DataMenager

### Bibliotecas utilizadas:
 - json
 - time
 - yaspin

Presente no arquivo **file_menager**, essa classe gerencia operações de leitura e escrita em um banco de dados armazenado em um arquivo JSON. Ele oferece métodos para ler o banco de dados inteiro ou dados específicos de um índice, obter dados com base em um elemento dentro de um índice específico e salvar novos dados no banco de dados, com feedback visual do processo de salvamento. O código também inclui um atraso artificial para simular operações demoradas e utiliza a biblioteca `yaspin` para criar efeitos visuais durante as operações de leitura e escrita.

## kit_menager.py

Como dito anteriormente, ainda será implementado.