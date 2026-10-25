# Projeto do aluno - Aula 11

## 1. Preparar o ambiente

```bash
python --version
python -m pip install -r requirements.txt
python -m pytest --version
python -m pytest -q
```

## 2. Exercicio formativo

Implemente, usando TDD:

```python
calcular_taxa_entrega(distancia_km, total_pedido)
```

### Regras obrigatorias

1. Ate 3 km, a taxa de entrega e R$ 5.
2. Acima de 3 km, acrescentar R$ 2 por quilometro excedente.
3. Pedidos a partir de R$ 100 possuem entrega gratuita.

### Tres cenarios obrigatorios

- 2 km e pedido de R$ 50: taxa de R$ 5;
- 4 km e pedido de R$ 50: taxa de R$ 7;
- 5 km e pedido de R$ 100: taxa de R$ 0.

### Desafio opcional

- distancia negativa deve gerar `ValueError`.

## 3. Processo esperado

Para cada comportamento:

1. escreva somente o teste desse comportamento;
2. execute e confirme a falha (Red);
3. implemente o minimo necessario (Green);
4. execute toda a suite;
5. passe ao proximo comportamento;
6. ao final, melhore a estrutura sem alterar o comportamento (Refactor).

Nao implemente as tres regras de uma vez.

## 4. Registro do ciclo

Use `REGISTRO_TDD.md` para registrar pelo menos um ciclo completo.

## 5. Exercicio compensatorio concluido

A funcao esta em `src/pedido.py`; os tres cenarios obrigatorios estao em
`tests/test_taxa_entrega.py`. Os quatro testes originais foram mantidos.

Consulte `REGISTRO_TDD.md` e `evidencias-tdd/` para acompanhar os tres ciclos
Red → Green e a refatoracao final. `relatorio-testes.txt` contem a execucao
final completa, com sete testes aprovados.

Para gerar o relatorio no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-testes.txt
```

No macOS/Linux, com o ambiente Python do projeto ativo:

```bash
python -m pytest -v | tee relatorio-testes.txt
```

## Observacao sobre venv

Na proxima aula sera utilizado `venv`, um ambiente virtual isolado que mantem os pacotes do projeto separados dos demais projetos Python.
