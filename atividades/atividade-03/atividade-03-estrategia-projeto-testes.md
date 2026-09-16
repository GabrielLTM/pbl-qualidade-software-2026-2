# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** Qualidade de Software 2026/02 — Senac RS (POA)  
**Equipe:** trabalho individual  
**Data:** 16/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gabriel Lessa Tramasol Machado | @GabrielLTM |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se o usuário autenticado consegue montar e concluir um pedido em um restaurante do LocalEats, se as quantidades e o valor total registrados no pedido correspondem exatamente ao que foi apresentado e confirmado no painel "Seu Pedido", e se o pedido em montagem é preservado durante a navegação do usuário pela aplicação. Não se pretende verificar todas as entradas possíveis do cardápio, e sim as situações em que um erro traria consequência financeira ou levaria ao abandono do pedido.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Gabriel Lessa Tramasol Machado | Fazer pedido | Montagem do pedido a partir do cardápio (adição e remoção de itens), cálculo do total exibido, condições em que a conclusão do pedido é permitida ou impedida, correspondência entre o total confirmado e o total registrado no histórico, e preservação do pedido em montagem durante a navegação. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Criar conta | Não faz parte do fluxo de conclusão do pedido escolhido para os testes. A verificação parte de uma conta de teste já cadastrada e autenticada, usada como pré-condição. |
| Favoritar e desfavoritar restaurantes | Não interfere na montagem nem na conclusão do pedido, e o risco associado tem impacto baixo: uma falha ali não gera cobrança indevida nem perda do pedido. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema, com um caso conduzido também como teste de aceitação do fluxo fim a fim | O que precisa ser verificado é o comportamento do fluxo completo pela interface: cardápio, painel do pedido, confirmação e histórico. O defeito de interesse aparece na integração dessas telas, não em uma unidade isolada. Não há acesso ao código para atuar em nível unitário. |
| Tipos de teste | Funcional | Os dois riscos priorizados são de regra de negócio e de comportamento esperado do fluxo (valor registrado e preservação do pedido). Desempenho, carga e segurança ficam fora desta rodada, por não estarem entre os riscos de maior prioridade para a funcionalidade escolhida. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | A verificação usa apenas entradas e saídas observáveis na interface pública da aplicação (itens escolhidos, total exibido, mensagens e conteúdo do histórico). Não há acesso ao código-fonte nem ao banco de dados, portanto não é possível derivar casos a partir da estrutura interna. |
| Técnicas de teste | Tabela de decisão (R01) e transição de estados (R02) | A conclusão do pedido depende da combinação de duas condições independentes (usuário autenticado e pedido com pelo menos um item), o que é exatamente o cenário da tabela de decisão. Já a perda do pedido em montagem é um problema de estado que sobrevive ou não a um evento de navegação, o que é melhor representado por transição de estados. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação em <https://local-eats-unisenac.vercel.app/>; navegador Google; conta de teste já autenticada; um restaurante com pratos de preços distintos no cardápio, como o "Restaurante Sabor 0"; página "Meus Pedidos" acessível. |
| Responsáveis pelo planejamento | Gabriel Lessa Tramasol Machado (trabalho individual) |
| Responsáveis pela especificação dos casos | Gabriel Lessa Tramasol Machado |
| Responsáveis pela futura execução | Gabriel Lessa Tramasol Machado |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação disponível e responsiva; conta de teste autenticada; cardápio carregando os pratos com preços visíveis; histórico de pedidos acessível; os três casos de teste especificados e revisados (CT01 a CT03, detalhados na seção 4.1). |
| Saída | Os três casos executados, com resultado obtido registrado e comparado ao resultado esperado; cada divergência registrada como defeito com passos de reprodução e evidência; nenhum defeito de prioridade alta relacionado ao valor do pedido em aberto sem análise. |
| Suspensão | Aplicação indisponível ou instável; impossibilidade de autenticar a conta de teste; cardápio sem pratos ou sem preços, o que impede verificar o cálculo do total; indisponibilidade da página "Meus Pedidos", que é onde o resultado esperado dos casos ligados ao R01 é observado. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|:---:|:---:|:---:|:---:|---|
| R01 | Gabriel Lessa Tramasol Machado | Fazer pedido | O pedido ser registrado com quantidade ou valor total diferente do que foi apresentado e confirmado no painel "Seu Pedido" (soma incorreta, item que não entra no total, erro de arredondamento em centavos ou perda da quantidade escolhida). | O usuário é cobrado por um valor que não aceitou, ou o restaurante recebe um pedido com valor menor do que o devido. Em ambos os casos há prejuízo financeiro, contestação no atendimento e perda de confiança na aplicação. | Média | Alto | **Alta** | O valor aparece como "Total" no painel do restaurante e depois como "Total Estimado" no histórico: duas telas, dois rótulos e dois momentos distintos, e a divergência entre eles é uma falha plausível. A probabilidade é média porque o cálculo observado para duas unidades estava correto (2 × R$ 59,17 = R$ 118,34), mas não foram verificadas combinações de pratos diferentes nem arredondamentos. O impacto é alto porque envolve dinheiro e atinge usuário e restaurante ao mesmo tempo. |
| R02 | Gabriel Lessa Tramasol Machado | Fazer pedido | O pedido em montagem ser descartado sem aviso quando o usuário sai da página do restaurante e retorna, obrigando-o a remontar a seleção. | O usuário perde o que já havia escolhido, não entende o motivo e tende a abandonar o pedido. O restaurante perde a venda, e o efeito é maior em pedidos com vários itens, em que remontar custa mais esforço. | Alta | Médio | **Alta** | A probabilidade é alta porque o comportamento foi observado na exploração da Atividade 1: um item adicionado deixou de constar ao navegar para "Meus Favoritos" e retornar ao mesmo restaurante, sem qualquer mensagem. Navegar entre o cardápio e outras páginas antes de fechar o pedido é um percurso comum. O impacto é médio, e não alto, porque não há perda financeira nem dado incorreto registrado: o prejuízo é a desistência do pedido. A combinação de probabilidade alta com impacto médio resulta em prioridade alta. |

### 3.2 Aplicação das técnicas

#### Análise do risco R01

**Integrante:** Gabriel Lessa Tramasol Machado  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R01  
**Técnica escolhida:** Tabela de decisão

**Por que a técnica foi escolhida:**  
A permissão para concluir o pedido não depende de um valor em uma faixa, e sim da combinação de duas condições independentes: o usuário estar autenticado e o pedido conter ao menos um item. Duas condições booleanas geram quatro combinações, e a tabela de decisão garante que nenhuma delas fique sem resultado esperado definido — inclusive a combinação que a interface hoje não oferece caminho para alcançar. Particionamento de equivalência ou análise de valor limite seriam adequados para faixas numéricas (uma quantidade máxima por item, por exemplo), mas não para a combinação de condições que determina se o pedido pode ser concluído e com qual valor.

**Aplicação da técnica:**

Condições: **C1** = usuário autenticado; **C2** = pedido contém pelo menos um item.

| Regra | C1: usuário autenticado? | C2: pedido com ao menos um item? | Resultado esperado |
|:---:|:---:|:---:|---|
| 1 | Sim | Sim | Concluir o pedido e registrá-lo no histórico com as mesmas quantidades e o mesmo valor total exibidos no painel "Seu Pedido" no momento da confirmação. |
| 2 | Sim | Não | Não oferecer a ação de conclusão e não registrar pedido algum. (Observado na exploração: ao remover o último item, o painel "Seu Pedido" desaparece junto com o botão "Finalizar Pedido".) |
| 3 | Não | Sim | Solicitar autenticação e não registrar o pedido enquanto ela não ocorrer; após autenticar, o conteúdo do pedido deve ser preservado. |
| 4 | Não | Não | Solicitar autenticação e não registrar pedido algum. |

As regras 1 e 2 são as que produzem os casos desta rodada, por serem as que envolvem o valor registrado e o limite entre "pode concluir" e "não pode concluir".

Sobre as regras 3 e 4, foi observado em uma sessão de navegador sem autenticação que a aplicação não exibe a lista de restaurantes nem o cardápio: o endereço da aplicação, a página de exploração e a página de detalhes de um restaurante levam todos à tela "Entrar". O resultado esperado é atendido, porque nenhum pedido é registrado sem autenticação. Como consequência, a **regra 3 (não autenticado, com itens no pedido) é uma combinação que a interface não permite alcançar**: não há como montar um pedido antes de entrar no sistema, e por isso ela não gera caso de teste.

Esse mesmo comportamento sugere, porém, uma inconsistência de usabilidade: exigir autenticação para apenas visualizar os restaurantes obriga o usuário a criar conta antes de saber se a aplicação oferece algo que lhe interesse. Seria razoável permitir a exploração do catálogo e solicitar a autenticação somente no momento de concluir o pedido — cenário que corresponde exatamente à regra 3. A observação fica registrada, mas não gera caso nesta rodada, por estar fora do risco priorizado.

**Casos derivados:** CT01 — impedir a conclusão de pedido sem itens, da regra 2; e CT02 — registrar no histórico o mesmo total confirmado no painel, da regra 1. Os dois estão especificados por completo na seção 4.1.

#### Análise do risco R02

**Integrante:** Gabriel Lessa Tramasol Machado  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R02  
**Técnica escolhida:** Transição de estados

**Por que a técnica foi escolhida:**  
O problema não está em um valor de entrada, mas na permanência de um estado quando um evento acontece. O pedido em montagem tem estados bem delimitados e o que precisa ser verificado é se o evento "navegar para outra página e retornar" preserva ou destrói esse estado. A técnica de transição de estados expõe exatamente esse tipo de defeito, porque obriga a declarar qual estado deveria valer depois de cada evento, incluindo os eventos que não deveriam mudar nada.

**Aplicação da técnica:**

O pedido em montagem pode estar em três estados, identificados pelo que aparece na tela:

- **Pedido vazio** — nenhum item escolhido e o painel "Seu Pedido" não aparece na página.
- **Pedido em montagem** — pelo menos um item escolhido, com o painel "Seu Pedido" exibindo as quantidades e o total.
- **Pedido enviado** — o pedido foi confirmado e passou a constar em "Meus Pedidos" com a situação "PENDING".

| # | Estado atual | Evento | Estado esperado | Situação |
|:---:|---|---|---|---|
| T1 | Pedido vazio | Acionar "Adicionar" em um prato | Pedido em montagem, com um item e o total correspondente | Transição válida |
| T2 | Pedido em montagem | Acionar "Adicionar" novamente no mesmo prato | Pedido em montagem, com a quantidade incrementada e o total recalculado | Transição válida |
| T3 | Pedido em montagem, com um item de quantidade 1 | Reduzir a quantidade desse item para zero | Pedido vazio, sem o painel "Seu Pedido" | Transição válida |
| T4 | **Pedido em montagem** | **Navegar para outra página e retornar ao mesmo restaurante** | **Pedido em montagem, com os itens preservados** | **Divergência observada (R02): o estado obtido foi "Pedido vazio"** |
| T5 | Pedido em montagem | Acionar "Finalizar Pedido" | Pedido enviado, constando em "Meus Pedidos" | Transição válida |
| T6 | Pedido vazio | Acionar "Finalizar Pedido" | Nenhuma mudança de estado: a ação não deve estar disponível e nenhum pedido deve ser registrado | Transição bloqueada |
| T7 | Pedido enviado | Acionar "Finalizar Pedido" novamente | Nenhuma mudança de estado: não deve ser gerado um segundo pedido com o mesmo conteúdo | Transição bloqueada |

A transição T4 é a única da tabela em que o estado obtido não corresponde ao esperado: na exploração da Atividade 1, ao retornar ao mesmo restaurante o painel "Seu Pedido" não estava mais presente e o item adicionado não constava mais, sem nenhuma mensagem ao usuário. É essa divergência que origina o risco R02 e o caso CT03, que passa a servir como caso de confirmação e de regressão — ou seja, deve falhar no comportamento atual e passar depois da correção. As transições T1, T2, T3 e T5 correspondem ao comportamento observado. As transições T6 e T7 ficam documentadas como bloqueios a verificar em uma próxima rodada.

**Casos derivados:** CT03 — preservar o pedido em montagem ao navegar e retornar ao restaurante, da transição T4. Especificado por completo na seção 4.1.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Impedir a conclusão de pedido sem itens

**Integrante responsável:** Gabriel Lessa Tramasol Machado  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01 (regra 2 da tabela de decisão)  
**Técnica utilizada:** Tabela de decisão

**Pré-condição:**  
Usuário autenticado na aplicação, na página de um restaurante com cardápio carregado (por exemplo "Restaurante Sabor 0") e sem nenhum item escolhido.

**Dados de entrada:**  
Prato: "Prato Especial 0" (R$ 59,17); quantidade final no pedido: zero.

**Passos:**

1. Acionar "Adicionar" no "Prato Especial 0" e confirmar que o painel "Seu Pedido" passou a exibir 1 item.
2. Reduzir a quantidade desse item para zero, usando o controle de remoção do painel.
3. Observar o painel "Seu Pedido" e procurar a ação de conclusão do pedido na página.
4. Abrir "Meus Pedidos".

**Resultado esperado:**  
Após a remoção, o painel "Seu Pedido" não apresenta itens e a ação "Finalizar Pedido" não está disponível na página. Em "Meus Pedidos" não surge nenhum pedido novo, e a quantidade de pedidos listados é a mesma de antes da execução.

---

### CT02: Registrar no histórico o mesmo total confirmado no painel do pedido

**Integrante responsável:** Gabriel Lessa Tramasol Machado  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01 (regra 1 da tabela de decisão)  
**Técnica utilizada:** Tabela de decisão

**Pré-condição:**  
Usuário autenticado, na página de um restaurante cujo cardápio tenha pratos de preços distintos ("Restaurante Sabor 0": R$ 59,17, R$ 46,81 e R$ 54,61). Registrar previamente a quantidade de pedidos existentes em "Meus Pedidos".

**Dados de entrada:**  
Duas unidades do "Prato Especial 0" (R$ 59,17) e uma unidade do "Prato Especial 1" (R$ 46,81). Total esperado: (2 × R$ 59,17) + R$ 46,81 = R$ 165,15.

**Passos:**

1. Acionar "Adicionar" duas vezes no "Prato Especial 0" e uma vez no "Prato Especial 1".
2. Anotar as quantidades e o valor total exibidos no painel "Seu Pedido".
3. Acionar "Finalizar Pedido" e aguardar a confirmação.
4. Abrir "Meus Pedidos" e localizar o pedido recém-criado.

**Resultado esperado:**  
O painel "Seu Pedido" exibe 3 itens e total de R$ 165,15. Após a confirmação, é apresentada a mensagem de pedido realizado, e em "Meus Pedidos" o pedido recém-criado apresenta as mesmas quantidades (2 unidades do primeiro prato e 1 do segundo) e "Total Estimado" de R$ 165,15, sem divergência de centavos em relação ao valor confirmado.

---

### CT03: Preservar o pedido em montagem ao navegar e retornar ao restaurante

**Integrante responsável:** Gabriel Lessa Tramasol Machado  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02 (transição T4)  
**Técnica utilizada:** Transição de estados

**Pré-condição:**  
Usuário autenticado, na página do "Restaurante Sabor 0", sem nenhum item escolhido e sem nenhum pedido em andamento.

**Dados de entrada:**  
Uma unidade do "Prato Especial 0" (R$ 59,17).

**Passos:**

1. Acionar "Adicionar" no "Prato Especial 0" e confirmar que o painel "Seu Pedido" exibe 1 item com total de R$ 59,17.
2. Acessar "Meus Favoritos" pelo menu superior, sem concluir o pedido.
3. Retornar à página do "Restaurante Sabor 0".
4. Observar o painel "Seu Pedido" e o total exibido.

**Resultado esperado:**  
Ao retornar, o pedido continua no estado "em montagem": o painel "Seu Pedido" apresenta 1 unidade do "Prato Especial 0" com total de R$ 59,17, e a ação "Finalizar Pedido" continua disponível. Caso a aplicação descarte deliberadamente o pedido em montagem, o descarte deve ser informado ao usuário antes de acontecer, e não de forma silenciosa.

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Gabriel Lessa Tramasol Machado | Fazer pedido | R01: pedido registrado com quantidade ou valor divergente do confirmado | Tabela de decisão | CT01 e CT02 |
| Gabriel Lessa Tramasol Machado | Fazer pedido | R02: pedido em montagem descartado sem aviso ao navegar | Transição de estados | CT03 |

**Leitura da matriz:** a funcionalidade "fazer pedido" foi analisada integralmente; foram identificados dois riscos, ambos de prioridade alta; foram aplicadas duas técnicas distintas, cada uma escolhida pela natureza do risco; os três casos de teste estão vinculados a um risco e a uma técnica, e nenhum dos dois riscos ficou sem caso de teste correspondente. As combinações documentadas mas não cobertas nesta rodada (regras 3 e 4 da tabela de decisão e transições T6 e T7) estão registradas como próximos casos, para que a lacuna fique explícita em vez de invisível.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Apoio na exploração da aplicação, na comparação entre as técnicas e na redação dos casos de teste.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
Foi sugerido aplicar análise de valor limite sobre a quantidade de itens do pedido. Rejeitei a sugestão porque o LocalEats não apresenta limite de quantidade, estoque nem valor mínimo: não há fronteira declarada para testar. A escolha passou a ser tabela de decisão.

**Como as respostas foram verificadas:**  
Confirmei na própria interface os comportamentos citados e recalculei os valores esperados a partir dos preços do cardápio. Os comportamentos ainda não executados estão marcados como esperados, e não como observados.
