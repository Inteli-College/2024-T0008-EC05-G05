---
title: Armazenamento dos Dados
sidebar_position: 6
---

## Introdução

Para o desenvolvimento de um sistema eficiente, optamos por uma estratégia híbrida no gerenciamento de dados, utilizando dois tipos de bancos de dados: um relacional e outro não relacional. Essa escolha de abordagem foi influenciada pela facilidade em explorar as vantagens específicas de cada tipo de banco de dados e atendendo às necessidades distintas do nosso projeto.

## Banco de Dados - SQLite

Para o armazenamento de informações sobre os kits, escolhemos o SQLite, um sistema de gerenciamento de banco de dados relacional. O SQLite oferece uma solução leve, sem a necessidade de um servidor de banco de dados dedicado, tornando-o ideal para nosso contexto. Utilizamos este banco de dados relacional por várias razões:

Organização e eficiência: Ao armazenar as informações dos kits em um banco de dados relacional, podemos aproveitar a organização estruturada e a integridade dos dados, facilitando consultas complexas e garantindo a consistência das informações.

Compatibilidade com a lógica do projeto: A escolha pelo SQLite reflete nossa necessidade de um sistema que suporte relações entre diferentes tipos de dados, essencial para a organização e gerenciamento dos kits conforme nossa lógica de projeto.

## Banco de Dados - TinyDB

Para o registro de logs do sistema, optamos pelo TinyDB, um banco de dados não relacional. A escolha de um banco de dados não relacional para esta função deve-se à natureza dos dados de log, que são:

Rápidos e Diretos: Os logs são gerados em alta velocidade e requerem uma inserção rápida, sem a necessidade de uma estrutura de dados complexa.

Sem Muita Organização: Diferentemente das informações dos kits, os logs não precisam de uma organização estruturada em tabelas relacionais. Eles são mais sobre registros temporais de eventos ou ações realizadas pelo sistema.

## Conclusão

Para entender mais profundamente sobre como o armazenamento se conecta com o restante da solução é recomendado consultar a sessão de arquitetura.