# Registro do ciclo de TDD

Data: 25/10/2026.

Os cenarios foram implementados um por vez. Os quatro testes originais de
`calcular_total` foram preservados. As saidas reais de cada execucao estao
no diretorio `evidencias-tdd/`.

## Ciclo 1: taxa inicial

**Teste criado:** `test_cobra_cinco_reais_para_dois_km_e_pedido_de_cinquenta_reais`.

**Red:** o teste nao pode ser coletado porque `calcular_taxa_entrega` ainda nao
existia, causando `ImportError` (codigo de saida 2).
Evidencia: [01-red.txt](evidencias-tdd/01-red.txt).

**Green:** criei a funcao retornando apenas `5`, o minimo para atender o primeiro
cenario. A suite completa passou: **5 passed**.
Evidencia: [01-green.txt](evidencias-tdd/01-green.txt).

**Refactor:** nenhuma alteracao estrutural foi necessaria neste ciclo.

## Ciclo 2: distancia excedente

**Teste criado:** `test_cobra_sete_reais_para_quatro_km_e_pedido_de_cinquenta_reais`.

**Red:** a funcao retornou `5` em vez de `7`; resultado: **1 failed, 5 passed**
(codigo de saida 1). Evidencia: [02-red.txt](evidencias-tdd/02-red.txt).

**Green:** acrescentei a regra `5 + (distancia_km - 3) * 2` para distancias acima
de 3 km. A suite completa passou: **6 passed**.
Evidencia: [02-green.txt](evidencias-tdd/02-green.txt).

**Refactor:** a estrutura foi mantida ate concluir o proximo comportamento.

## Ciclo 3: entrega gratuita

**Teste criado:** `test_entrega_gratuita_para_cinco_km_e_pedido_de_cem_reais`.

**Red:** a funcao retornou `9` em vez de `0`; resultado: **1 failed, 6 passed**
(codigo de saida 1). Evidencia: [03-red.txt](evidencias-tdd/03-red.txt).

**Green:** acrescentei o retorno antecipado de `0` quando `total_pedido >= 100`,
antes do calculo por distancia. A suite completa passou: **7 passed**.
Evidencia: [03-green.txt](evidencias-tdd/03-green.txt).

## Refactor final

Substitui os dois retornos da taxa paga por um unico calculo, usando
`distancia_excedente = max(distancia_km - 3, 0)`. Acrescentei anotacoes de tipo
e documentei as regras na funcao. A gratuidade continua tendo prioridade.

**Resultado final:** os sete testes passaram apos a refatoracao: os tres novos
cenarios obrigatorios e os quatro testes originais.
Evidencia: [relatorio-testes.txt](relatorio-testes.txt).

O relatorio foi gerado no macOS com `python -m pytest -v | tee relatorio-testes.txt`,
equivalente ao comando PowerShell indicado na atividade. Nao foi implementado
o desafio opcional de rejeitar distancia negativa.
