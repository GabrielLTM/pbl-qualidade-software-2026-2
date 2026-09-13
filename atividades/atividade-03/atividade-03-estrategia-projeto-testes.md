# Atividade 3: Estratégia e Projeto de Testes do LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [preencher]  
**Equipe:** [preencher, se aplicável]  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [nome] | [@usuario] |
| [nome] | [@usuario] |
| [nome] | [@usuario] |
| [nome] | [@usuario] |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

[Expliquem brevemente o que a equipe pretende verificar com os testes.]

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| [nome] | [funcionalidade] | [preencher] |
| [nome] | [funcionalidade] | [preencher] |
| [nome] | [funcionalidade] | [preencher] |
| [nome] | [funcionalidade] | [preencher] |

> Acrescentem ou removam linhas conforme o número de integrantes.

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| [preencher] | [preencher] |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | [preencher] | [preencher] |
| Tipos de teste | [preencher] | [preencher] |
| Perspectiva caixa-preta ou caixa-branca | [preencher] | [preencher] |
| Técnicas de teste | [preencher] | [preencher] |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | [preencher] |
| Responsáveis pelo planejamento | [preencher] |
| Responsáveis pela especificação dos casos | [preencher] |
| Responsáveis pela futura execução | [preencher] |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | [O que precisa estar disponível antes do início dos testes?] |
| Saída | [O que precisa ser atendido para considerar os testes concluídos?] |
| Suspensão | [Em quais situações os testes deverão ser interrompidos?] |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

> Cada integrante deve analisar pelo menos um risco relacionado à funcionalidade escolhida. No trabalho individual, devem ser analisados dois riscos.

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | [nome] | [funcionalidade] | [o que pode dar errado] | [quem será afetado e como] | [Baixa/Média/Alta] | [Baixo/Médio/Alto] | [Baixa/Média/Alta] | [preencher] |
| R02 | [nome] | [funcionalidade] | [o que pode dar errado] | [quem será afetado e como] | [Baixa/Média/Alta] | [Baixo/Médio/Alto] | [Baixa/Média/Alta] | [preencher] |

> Acrescentem as linhas necessárias e mantenham identificadores únicos: R01, R02, R03 etc.

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** [nome]  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R01]  
**Técnica escolhida:** [particionamento de equivalência, análise de valor limite, tabela de decisão ou transição de estados]

**Por que a técnica foi escolhida:**  
[Expliquem por que a técnica é adequada à regra ou ao risco analisado.]

**Aplicação da técnica:**  
[Apresentem as classes, limites, combinações ou transições identificadas. Utilizem uma tabela ou lista quando necessário.]

**Casos derivados:** [CT01 e CT02]

#### Análise do integrante 2

**Integrante:** [nome]  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R02]  
**Técnica escolhida:** [preencher]

**Por que a técnica foi escolhida:**  
[preencher]

**Aplicação da técnica:**  
[preencher]

**Casos derivados:** [preencher]

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [R01 ou descrição do requisito]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[O que precisa existir ou estar preparado antes da execução.]

**Dados de entrada:**  
[Valores ou dados necessários. Caso não sejam necessários, registrem “Não se aplica”.]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou.]

---

### CT02: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [preencher]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[preencher]

**Dados de entrada:**  
[preencher]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[preencher]

---

> Copiem o modelo acima e continuem a numeração para criar os demais casos: CT03, CT04, CT05 etc.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| [nome] | [funcionalidade] | [R01 ou requisito] | [técnica] | [CT01 e CT02] |
| [nome] | [funcionalidade] | [R02 ou requisito] | [técnica] | [CT03 e CT04] |

> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[Descrever brevemente. Caso nenhuma sugestão tenha sido rejeitada, expliquem como as sugestões foram analisadas criticamente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
