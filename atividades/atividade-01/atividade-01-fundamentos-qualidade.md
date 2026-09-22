# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software 2026/02 — Senac RS (POA)  
**Equipe:** trabalho individual  
**Data:** 16/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gabriel Lessa Tramasol Machado | @GabrielLTM |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | O usuário autenticado deve conseguir selecionar pratos do cardápio de um restaurante e concluir o pedido (funcionalidade "fazer pedido" descrita no escopo da aplicação). | Usuário consumidor e restaurante local | A aplicação deixa de cumprir seu propósito central: o usuário não consegue comprar e o restaurante não recebe demanda, restando apenas um catálogo de consulta. |
| Explícita | O usuário deve conseguir consultar os pedidos já realizados (funcionalidade "consultar pedidos" descrita no escopo da aplicação). | Usuário consumidor | O usuário perde o registro do que pediu e do valor combinado, ficando sem base para conferir a entrega ou contestar uma cobrança. |
| Implícita | O pedido em montagem não deve ser descartado sem aviso quando o usuário navega para outra página da aplicação e retorna ao mesmo restaurante. | Usuário consumidor e restaurante local | O usuário precisa remontar a seleção sem entender o motivo, o que aumenta o abandono do pedido e reduz a conversão do restaurante. |
| Implícita | O histórico de pedidos deve identificar restaurante e pratos pelos nomes exibidos no cardápio, e não por identificadores internos do sistema. | Usuário consumidor e atendimento do restaurante | O usuário não reconhece o próprio pedido no histórico, não consegue conferir o que foi comprado e o atendimento perde uma referência comum para tratar dúvidas e reclamações. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. No LocalEats as funcionalidades "fazer pedido" e "consultar pedidos" existem e funcionam: o pedido foi concluído e passou a constar no histórico. Ainda assim, o histórico apresenta o pedido como "Restaurante ID: 1" e "2x Item Id #1", em vez dos nomes "Restaurante Sabor 0" e "Prato Especial 0" mostrados no cardápio. A necessidade implícita de reconhecer o próprio pedido não é atendida, e o usuário fica sem conferir o que comprou. Ou seja, qualidade não é a presença da funcionalidade, mas o atendimento das necessidades explícitas **e** implícitas de quem usa o sistema.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Gabriel Lessa Tramasol Machado | Fazer pedido | **Uso esperado:** em "Restaurante Sabor 0" (restaurant.html?id=1), acionei "Adicionar" duas vezes no "Prato Especial 0" (R$ 59,17) e confirmei em "Finalizar Pedido"; depois abri "Meus Pedidos". **Uso alternativo/incompleto:** adicionei um item ao pedido, saí da página do restaurante para "Meus Favoritos" e retornei ao mesmo restaurante sem concluir o pedido. | **Uso esperado:** o painel "Seu Pedido" exibiu "2 Itens", "2x Prato Especial 0 — R$ 118,34" e "Total: R$ 118,34"; após confirmar, apareceu a mensagem "Pedido Realizado! Seu pedido de teste foi enviado com sucesso."; em "Meus Pedidos" o pedido #269 passou a constar com situação "PENDING" e "Total Estimado: R$ 118,34", porém descrito como "Restaurante ID: 1" e "2x Item Id #1", sem os nomes do restaurante e do prato. **Uso alternativo:** ao retornar ao mesmo restaurante, o painel "Seu Pedido" não estava mais presente e o item adicionado não constava mais; nenhuma mensagem foi exibida antes ou depois do descarte. Também observei que, ao reduzir a quantidade do único item para zero, o painel desaparece e a ação "Finalizar Pedido" deixa de ser oferecida, o que corresponde ao comportamento esperado. | [carrinho com 2 itens e total](evidencias/gabriel-fazer-pedido-carrinho-2-itens-total.png) · [confirmação do pedido](evidencias/gabriel-fazer-pedido-confirmacao-pedido-realizado.png) · [histórico com identificadores internos](evidencias/gabriel-fazer-pedido-meus-pedidos-ids-tecnicos.png) · [item no pedido antes de navegar](evidencias/gabriel-fazer-pedido-item-adicionado-antes-de-navegar.png) · [pedido vazio após retornar](evidencias/gabriel-fazer-pedido-carrinho-vazio-apos-voltar.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Gabriel Lessa Tramasol Machado | Ao finalizar o pedido, as quantidades e o valor total registrados e exibidos em "Meus Pedidos" devem ser idênticos aos apresentados no painel "Seu Pedido" no momento da confirmação, para qualquer combinação de pratos e quantidades do cardápio. | Adequação funcional → Correção funcional (ISO/IEC 25010) | O valor que o usuário aceita aparece como "Total" no painel do restaurante, e o valor que fica registrado aparece como "Total Estimado" no histórico: duas telas e dois rótulos diferentes, sem garantia de serem o mesmo número. Se divergirem, o usuário é cobrado por um valor que não aceitou ou o restaurante recebe menos do que o devido. É correção funcional, e não usabilidade, porque a falha seria um número errado, não uma tela difícil de entender. | Montar pedidos com combinações diferentes (1 item; 2 unidades do mesmo prato; dois pratos de preços distintos) e, em cada um, comparar o "Total" do painel com o "Total Estimado" do histórico, além das quantidades. Contar quantos pedidos divergiram sobre o total montado, registrando o valor esperado e o obtido. Os preços quebrados do cardápio (R$ 59,17, R$ 46,81) tornam os centavos o ponto de atenção. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Apoio na organização e revisão do documento.

**Como as respostas foram verificadas:**  
Conferi cada afirmação contra a evidência correspondente em `evidencias/` e recalculei os valores (2 × R$ 59,17 = R$ 118,34). O requisito, a característica escolhida e a forma de avaliar foram revisados e assumidos por mim.
