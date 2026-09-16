# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software 2026/02 — Senac RS (POA)  
**Equipe:** trabalho individual  
**Data:** 16/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gabriel Lessa Tramasol Machado | @GabrielLTM |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| ID | Problema identificado | Possível consequência para o produto ou para a equipe |
|:---:|---|---|
| P1 | Não existe um critério compartilhado de "pronto": cada pessoa decide por conta própria quando a funcionalidade está concluída, e os critérios de aceitação não são escritos antes da implementação. | Funcionalidades são declaradas prontas sem verificação mínima e chegam com defeitos ao usuário. A equipe passa a gastar em retrabalho e correção o tempo que deixou de gastar em prevenção, e discussões sobre "estava pronto ou não" se repetem a cada entrega. |
| P2 | A qualidade é tratada como etapa final e atribuição exclusiva do QA: parte da equipe entende que somente o QA deve testar. | O QA se torna gargalo e ponto único de falha, e os defeitos passam a ser descobertos no fim do fluxo, quando corrigir custa mais. O desenvolvedor não se apropria dos testes do próprio código e o produto fica dependente de uma única pessoa para avançar. |
| P3 | Papéis e responsabilidades não estão formalizados: defeitos são identificados mas nem sempre registrados e acompanhados, não está claro quem pode aprovar a disponibilização de uma nova versão e algumas atividades têm responsável duplicado enquanto outras não têm nenhum. | Defeitos conhecidos reaparecem em produção porque não há registro nem acompanhamento. A liberação de versão passa a depender de combinação informal, o que gera versões publicadas sem parecer de teste e, ao mesmo tempo, atividades paradas esperando alguém que ninguém designou. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade do LocalEats é construída ao longo de todo o desenvolvimento: o responsável pelo produto define critérios de aceitação verificáveis, o desenvolvedor escreve testes e participa da revisão de código, o DevOps garante ambiente e rastreabilidade das versões, e o QA projeta e conduz a verificação do sistema. Concentrar tudo no QA transforma a qualidade em uma inspeção no fim da fila: o defeito é descoberto quando já está caro de corrigir e a equipe perde o controle sobre o próprio trabalho. O QA é o especialista que define estratégia, técnicas e critérios, e não a única pessoa autorizada a testar.

---

## 3. Tarefa 2: Papéis e competências

### 3.1 Papéis definidos como necessários

Para organizar a qualidade no desenvolvimento do LocalEats foram definidos quatro papéis, que são os utilizados nas colunas da matriz da Tarefa 3.

| Papel | Por que é necessário no LocalEats |
|---|---|
| Responsável pelo produto (PO) | Escreve os critérios de aceitação e decide a prioridade entre corrigir defeito e entregar nova funcionalidade; responde pela decisão de liberar a versão. |
| Desenvolvedor | Implementa as funcionalidades e é quem pode impedir o defeito na origem, com testes unitários e revisão de código. |
| QA / analista de qualidade | Define a estratégia de testes, projeta os casos com técnicas adequadas e mantém o acompanhamento dos defeitos até o reteste. |
| DevOps | Mantém os ambientes e a esteira de publicação, e garante a rastreabilidade de qual versão está em produção. |

### 3.2 Papel analisado

A análise detalhada corresponde a um papel por integrante. No trabalho individual, o papel analisado é o de **desenvolvedor**, por ser o papel que atua na origem do defeito e que aparece na lacuna identificada na Tarefa 3.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Gabriel Lessa Tramasol Machado | Desenvolvedor | Implementar a funcionalidade atendendo aos critérios de aceitação acordados; criar e manter os testes unitários do próprio código; revisar o código de colegas antes da integração; registrar os defeitos que encontra, inclusive os próprios; corrigir os defeitos priorizados sem introduzir regressão; sinalizar requisito ambíguo antes de codificar, em vez de decidir por conta própria. | Domínio da linguagem e do framework do LocalEats; escrita de testes unitários e de integração; controle de versão e prática de revisão de código; depuração a partir de um relato de defeito; noções de desempenho e de segurança em aplicação web, para reconhecer quando a própria alteração cria risco. | Receber e dar feedback técnico sem levar para o campo pessoal; cuidado com o detalhe, inclusive no que não foi pedido explicitamente; pensamento crítico para questionar requisito ambíguo em vez de adivinhar; colaboração com o QA como parceiro de verificação, e não como inspetor. |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA | DevOps |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R, A | C | C | I |
| Revisar requisitos | A | R | R | I |
| Implementar a funcionalidade | I | R, A | C | I |
| Revisar o código | — | R, A | I | C |
| Criar testes unitários | I | R, A | C | — |
| Planejar e executar testes do sistema | C | R | R, A | I |
| Registrar e acompanhar defeitos | I | R | R, A | R |
| Priorizar a correção dos defeitos | R, A | C | C | C |
| Aprovar a disponibilização da versão | A | I | C | R |

**Verificação das regras:** todas as nove atividades possuem pelo menos um **R** e exatamente um **A**. Nas atividades em que o mesmo papel executa e responde pelo resultado (implementar, revisar código, criar testes unitários), o papel acumula **R** e **A**. Na aprovação da versão, o DevOps executa a publicação (**R**) e o responsável pelo produto decide se ela ocorre (**A**), com parecer técnico do QA (**C**).

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
A atividade "Revisar o código" ficou concentrada em um único papel, o desenvolvedor, acumulando **R** e **A**. Como executor e aprovador são o mesmo papel, nada na matriz impede que o autor da alteração seja também quem aprova a própria revisão — um conflito de interesse, porque quem escreveu o código tende a não enxergar a falha que acabou de introduzir. O mesmo padrão aparece, de forma mais branda, em "Registrar e acompanhar defeitos", com três papéis como **R**: o contexto relata que algumas atividades são realizadas por mais de uma pessoa e outras não possuem responsável definido, e responsabilidade compartilhada sem um **A** claro tende a virar responsabilidade de ninguém — por isso o QA foi mantido como aprovador dessa atividade.

**Consequência:**  
Defeitos que a revisão de código deveria interceptar seguem para o teste de sistema ou para produção, o que aumenta o custo da correção e reforça exatamente o problema relatado pela equipe: funcionalidades chegando ao usuário com defeito. Para mitigar, a regra adotada é que a revisão deve ser feita por um desenvolvedor diferente do autor da alteração, e que o **A** da revisão é sempre o revisor, nunca o autor. Se não houver outro desenvolvedor disponível para revisar, o QA entra como **C** obrigatório antes da integração.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| **Definition of Done acordada e visível.** Os critérios de aceitação são escritos de forma verificável antes da implementação, e nenhuma alteração é integrada sem cumprir quatro itens obrigatórios: (1) critérios de aceitação atendidos; (2) testes unitários criados pelo desenvolvedor; (3) revisão de código feita por outra pessoa; (4) teste de sistema executado. | **P1 (não existe critério compartilhado de "pronto"):** passa a existir um critério único e visível para integrar, em vez de cada pessoa decidir por conta própria. **P2 (qualidade tratada como atribuição exclusiva do QA):** os itens 2 e 3 da lista são cumpridos pelo desenvolvedor antes de qualquer teste de sistema, então a verificação deixa de ser uma etapa posterior a cargo do QA. | Responsável pelo produto define e aprova os critérios de aceitação; desenvolvedor cumpre e evidencia os itens da lista; QA propõe os itens de verificação e confirma o atendimento. |
| **Fluxo único de registro e triagem de defeitos**: todo defeito encontrado por qualquer papel é registrado no mesmo quadro, com passos de reprodução, evidência e severidade; uma triagem periódica curta define prioridade, responsável e prazo, e nenhum defeito é fechado sem reteste. | **P3 (defeitos identificados não são registrados nem acompanhados, e há atividades sem responsável definido):** cria rastreabilidade do defeito até o reteste e dá um dono a cada defeito, evitando que a decisão sobre o que corrigir aconteça por conversa informal. | QA (mantém o fluxo e aprova o fechamento), desenvolvedor (registra e corrige), responsável pelo produto (prioriza), DevOps (registra os defeitos observados em produção e no monitoramento). |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Apoio na organização do diagnóstico, na redação das tabelas e na revisão da matriz RACI.

**Como as respostas foram verificadas:**  
Revisei a matriz linha por linha contra as regras do enunciado (pelo menos um **R** e exatamente um **A** por atividade) e confirmei que cada prática recomendada corresponde a um dos problemas diagnosticados.
