---
title: Sistema de Logs 
sidebar_position: 6
---

## Introdução 

Em um sistema, ter o controle preciso de quem executou determinadas ações e quando essas ações ocorreram é fundamental para garantir a rastreabilidade e segurança. Para atender a esses requisitos, foram desenvolvidos três sistemas de logs distintos.

O sistema de logs da Api é responsável por armazenar todas as informações que o usuário envia para o robô. Já o sistema de logs do Dobot é capaz de armazenar todos os movimentos que o robô fez.
Por fim, o sistema de logs do backend é capaz de registrar quem e quando foram feitas alterações na composição dos kits.  

## Logs da API 

O sistema de log das requisições feitas para a API é responsável por armazenar todas as informações enviadas pelos usuários para o robô. Este sistema, implementado como um middleware, registra todas as requisições efetuadas para a API. Os logs estão armazenados no arquivo `\2024-T0008-EC05-G05\src\WebToRobot\request_log.json`

#### Estrutura do Log API

- **timestap**: Data e hora da requisição (String).
- **client_ip**: Endereço IP do cliente que fez a requisição (String).
- **user_agent**: Informações sobre o navegador do cliente (String).
- **method**: Método HTTP da requisição (String).
- **url**: URL da requisição (String).
- **query_params**: Parâmetros da requisição (Dicionário).
  


#### Estrutura do Log Dobot
Também a log das ações feitas pelo robô, que está localizado no arquivo `\2024-T0008-EC05-G05\src\WebToRobot\dobot_log.json`. A estrutura do log é a seguinte:

- **timestap**: Data e hora da ação (String).
- **action**: Ação realizada pelo robô (String).
- **details**: Detalhes da ação (String).
    


## Logs do backend 
O funcionamento do log do backend se dá quando um usuário decidi fazer uma atualização dentro de um kit na tela de estoque. Ao realizar a atualização é chamada a rota de update que executa a função de criar os logs. 

Os logs que informam atualizações no kit podem ser encontrados no seguinte caminho `2024-T0008-EC05-G05/src/api/warehouse` dentro da pasta `warehouse` há o arquivo `logs.json`. Dentro desse arquivo está disponível o log com todas as mudanças realizadas. 

#### Estrutura do log backend
As informações que ficam salvas no log do backend são relativamente simples e permitem um controle fácil do admin do sistema. 

- **kit_id**: ID do kit que foi atualizado.
- **update_time**: Data e hora que foi atualizado o kit.
- **windows_username**: Nome de usuário do windows de quem fez a atualização.

## Conclusão

Assim, com o sistema de logs há o controle de todas as alterações e requisições que foram feitas no projeto. 