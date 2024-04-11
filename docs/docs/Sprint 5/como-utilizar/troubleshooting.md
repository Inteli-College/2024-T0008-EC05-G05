---
title: Problemas Comuns
sidebar_position: 2
---

# Problemas Comuns

Aqui você encontrará uma lista de problemas comuns que podem ocorrer durante a utilização da solução desenvolvida pelo grupo e como resolvê-los.

## Problemas com a comunicação do robô



**Problema:** A API não está se comunicando com o frontend.

> **Solução:** Verifique se o IP do servidor está correto no arquivo `src/frontend/src/components/kit_description_popup/KitDescriptionPopup.js` e se o servidor está rodando.
**Problema:** O robô não está se movendo.

> **Solução 1:** Verifique se o robô está ligado e se a API `bot .py`de comunicação com o robô está rodando. Se não estiver, execute o comando `python bot.py`.
> **Solução 2:** Quando o programa `bot.py` é executado, ele procurar automaticamente a porta que o robô está conectado então verifique se o robô está ligado e consegui se conectar com o computador.
## Problemas com a comunicação do Raspberry Pico

**Problema:** O sensor de distância não está funcionando.

> **Solução 1:** Verifique se o IP do servidor está correto no arquivo `src/CodigoRasp/UltraSonico.py` e se o servidor está rodando.
> **Solução 2:** Verifique se o Raspberry Pico está ligado e se o código `UltraSonico.py` está rodando.
**Problema:** O sensor de distância está medindo a distância errada.

> **Solução:** Verifique se não foi trocado os pinos do sensor de distância.