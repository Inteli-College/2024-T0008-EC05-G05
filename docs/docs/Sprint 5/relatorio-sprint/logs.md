---
title: Logs
sidebar_position: 3
---


## Sistema de logs

Os logs de um sistema são registros que indicam de forma um pouco mais detalhada as ações realizadas. Dentro do contexto do nosso projeto, um exemplo de log seria o detalhamento da data e hora de modificação de um kit, qual kit foi modificado, e qual usuário realizou esta ação.

O monitoramento desses logs é importante para identificar o que aconteceu em um determinado momento, diagnosticar problemas, ter uma ideia quantitativa da produção de kits e até mesmo detectar atividades suspeitas.

Para armazenar essas informações, estamos utilizando o TinyDB como banco de dados, por ser uma forma facilitada de armazenar informações em formato json, tendo em vista que o funcionamento do robô também gera logs.

Os arquivos json que estão servindo de banco de dados para fazer os logs são: ```log_kits_items.json``` e ```user_activities.json```, que podem ser encontrados em ``` src/backend/logs-db````.

Em *log_kits_items.json*, há dois dicionários: um que contém apenas os itens e seus respectivos ids, e outro que guarda informações dos kits em si, como seus ids, seu tipo, data e itens. Com essas informações que é possível visualizar na tela de Dashboards quais itens foram utilizados e quantos kits foram produzidos a partir de uma filtragem de tempo - mês, semana e dia.
Antes essa lógica possuía um backend modularizado, mas para tornar a execução do projeto mais simples, decidimos unir o backend da página de dashboards com a nossa aplicação web como um todo.

Em *user_activities,json*, são registradas informações de ações dentro da plataforma, como por exemplo a edição de um kit. O dicionário contém qual usuário está acessando (se é administrador ou não), data e hora, qual ação foi realizada e qual kit foi modificado. Essas informações estão sendo guardadas pela lógica do arquivo ```Stock.py```, onde está o backend da página de estoques (e também onde acontece as edições dos kits).

