---
title: Desenvolvimento Web
sidebar_position: 1
---

# O que foi feito?

Durante esta sprint, foram desenvolvidos os modelos iniciais da aplicação web da solução. Isso inclui a tela de login, a tela inicial e a tela de suprimentos, com seus componentes já funcionais e conectados a um banco de dados de teste.

## Tela de Login

Ao acessar o site, a primeira tela que aparecerá é a tela de login. Nela, será necessário informar o e-mail e senha do usuário para fazer a autenticação. Isso permite a divisão de autorizações, onde diferentes usuários têm permissões específicas. Por exemplo, apenas uma pessoa autorizada pode criar ou modificar um pré-cadastro de um kit, em vez de qualquer usuário que acesse o site.

<div align="center"> 

**Imagem 2 - Tela inicial** 

![Tela Inicial](<../../../static/img/site-screens/Captura de tela 2024-03-17 191100.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

Ao finalizar essa etapa e clicar em **Login** ou pressionar `Enter`, o usuário será direcionado para a tela principal.

## Tela Principal

Na tela principal, vários elementos são encontrados, divididos em três seções. À esquerda, encontra-se a "sidebar" ou menu lateral. No centro, há a zona de visualização dos kits salvos. E, à direita, está a zona dos kits na fila de produção.

<div align="center"> 

**Imagem 2 - Tela inicial** 

![Tela Inicial](<../../../static/img/site-screens/Captura de tela 2024-03-17 215442.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

### Sidebar

A sidebar, ou menu lateral, permite a livre movimentação do usuário entre as páginas da aplicação web. Cada ícone do menu lateral redireciona o usuário para uma rota específica do servidor.

Por ser um componente simples, mas importante, foi adicionado destaque ao clicar nele, para chamar a atenção do usuário para esse elemento, facilitando a escolha da página desejada.

Dentro da sidebar, é possível redirecionar-se para a tela de kits, ainda em desenvolvimento, onde estarão apenas os kits salvos, além de haver a possibilidade de editar os kits existentes. Em seguida, há a tela de rota do estoque, onde será possível ver os itens salvos em cada posição pré-definida. Na terceira posição, está o ícone de redirecionamento para a tela de configurações do robô, também em desenvolvimento, onde será possível ajustar a velocidade de trabalho do robô e sua aceleração de movimentação. Por fim, os dashboards permitem acompanhar os kits mais produzidos e os itens mais utilizados.

<div align="center">

**Imagem 3 - Sidebar recolhida**

![Sidebar Recolhida](<../../../static/img/site-screens/Captura de tela 2024-03-17 215445.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

<div align="center">

**Imagem 4 - Sidebar extendida**

![Sidebar Extendida](<../../../static/img/site-screens/Captura de tela 2024-03-17 215456.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

### Zona de Kits Salvos

Essa região é crucial para iniciar a produção dos kits, pois é onde os kits salvos são exibidos, permitindo ao usuário iniciar a fabricação deles.

Para facilitar o entendimento do usuário, os kits foram apresentados em cards, contendo informações breves, como o nome, uma breve descrição, uma foto e dois botões. Um botão inicia a fabricação do kit, enquanto o outro permite editar as informações do mesmo e os itens presentes no kit. Vale ressaltar que esse segundo botão só será funcional para pessoas autorizadas a realizar esse tipo de alteração.

<div align="center">

**Imagem 5 - Região de Kits Salvos**

![Kits Salvos](<../../../static/img/site-screens/Captura de tela 2024-03-17 215443.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

### Zona de Kits em Produção

Esta zona mostra ao usuário o que está sendo produzido e o que está na fila de espera para produção. Com isso, é possível organizar os itens que serão utilizados na montagem dos kits. Essa área também utiliza cards para facilitar a compreensão das informações.

Vale ressaltar que atualmente nada pode ser feito nessa região. No entanto, está em desenvolvimento a funcionalidade de excluir itens da fila de espera de produção.

<div align="center">

**Imagem 6 - Região de Fila de Espera de Produção**

![Fila de Espera de Produção](<../../../static/img/site-screens/Captura de tela 2024-03-17 215444.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

### Tela de Estoque

A tela de gestão de estoque de kits oferece uma visão detalhada e a capacidade de alterar o conteúdo dos kits ao usuário. Ela permite a inclusão ou remoção de itens de forma simples, podendo escolher o que irá em cada caixa, possibilitando ajustes rápidos para satisfazer requisitos específicos dos clientes ou atualizar o inventário com novidades

Após as alterações, o sistema atualiza automaticamente o estoque, mantendo a precisão das informações e evitando desencontros logísticos. Essa eficiência assegura que o inventário reflita as últimas configurações dos kits, otimizando a satisfação do cliente e a eficácia operacional. 

<div align="center">

**Imagem 7 - Tela de Estoque**

![Tela de Estoque](<../../../static/img/site-screens/estoque-inicio.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>

O usuário poderá selecionar o kit desejado, clicar em "mostrar estoque" e editar os itens do kit conforme desejado. A imagem número 8 descreve esse processo:

<div align="center">

**Imagem 8 - Tela de Estoque com kit e itens selecionados**

![Tela de Estoque com kit e itens selecionados](<../../../static/img/site-screens/estoque-kits.png>)

**Fonte:** Elaborado pela equipe Cardio-Bot 

</div>
