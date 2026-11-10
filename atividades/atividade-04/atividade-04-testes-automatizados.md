# Atividade 4: testes automatizados do LocalEats

## 1. Identificação

- **Turma:** ADS5N26-2 — Qualidade de Software, Senac RS (POA).
- **Modalidade:** individual.
- **Integrante:** Gabriel Lessa Tramasol Machado (@GabrielLTM).
- **Repositório:** [pbl-qualidade-software-2026-2](https://github.com/GabrielLTM/pbl-qualidade-software-2026-2).
- **Diretório da atividade:** [atividade-04](./).
- **Última execução:** 09/11/2026.

## 2. Responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
| --- | --- | --- | --- | --- |
| TU01 | Gabriel Lessa Tramasol Machado | Unitário | R$ 30,00 atinge o mínimo | `test_regras_localeats.py::test_pedido_de_trinta_reais_atinge_o_minimo` |
| TU02 | Gabriel Lessa Tramasol Machado | Unitário | Um valor negativo gera `ValueError` | `test_regras_localeats.py::test_pedido_com_valor_negativo_gera_erro` |
| TU03 | Gabriel Lessa Tramasol Machado | Unitário | R$ 29,99 fica abaixo do mínimo | `test_regras_localeats.py::test_pedido_de_um_centavo_abaixo_do_minimo_nao_atinge_o_minimo` |
| TF01 | Gabriel Lessa Tramasol Machado | Funcional | A tela alterna entre os formulários de entrada e cadastro | `test_localeats.py::test_alterna_entre_formularios_de_entrada_e_cadastro` |

## 3. Regra e testes unitários

A função `pedido_atingiu_valor_minimo`, em [regras_localeats.py](regras_localeats.py), retorna `True` para R$ 30,00 ou mais, retorna `False` para valores não negativos abaixo do mínimo e lança `ValueError` para valores negativos. Os [testes unitários](test_regras_localeats.py) cobrem o valor exato do mínimo, um centavo abaixo e um centavo negativo.

## 4. Registro do TDD

1. **Primeiro teste (TU01).** A chamada com R$ 30,00 deveria retornar `True`. A primeira execução falhou com `NotImplementedError` porque a função ainda estava vazia. A comparação `valor_pedido >= 30` fez o teste passar.
2. **Segundo teste (TU02).** A chamada com −R$ 0,01 deveria lançar `ValueError`. O teste falhou porque a comparação retornava `False`. A validação de valores negativos passou a acontecer antes da comparação, e os dois testes passaram.
3. **Caso de borda (TU03).** O teste com R$ 29,99 passou com a mesma implementação. A função ficou com uma validação de entrada e uma comparação, sem necessidade de refatoração.

## 5. Teste funcional com Playwright

O [TF01](test_localeats.py) abre o [LocalEats](https://local-eats-unisenac.vercel.app/) em uma sessão de navegador limpa e confirma que o formulário de entrada está visível. Ao clicar em **Criar Conta**, verifica que o botão **Registrar** aparece e o formulário de entrada fica oculto. Ao clicar em **Entrar**, verifica que o botão de envio do formulário de entrada aparece e que o cadastro fica oculto.

O teste usa locators para delimitar cada formulário e assertions com espera automática do Playwright. As interações se limitam à alternância dos formulários. Resultado no Chromium: **aprovado**.

## 6. Resultado da execução

- **Total:** 4 testes.
- **Aprovados:** 4.
- **Reprovados:** 0.
- **Relatório:** [relatorio-pytest.txt](relatorio-pytest.txt).

A partir de `atividades/atividade-04/`, em um ambiente Python 3.12, instale as dependências e o navegador:

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Para executar e atualizar o relatório no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

No macOS ou Linux:

```sh
set -o pipefail
python -m pytest -v | tee relatorio-pytest.txt
```

## 7. Explicação individual

O TF01 verifica se a tela mostra apenas o formulário correspondente à ação escolhida. O contexto do navegador começa sem sessão autenticada. Após clicar em **Criar Conta**, o botão **Registrar** deve aparecer dentro do cadastro e a entrada deve ficar oculta. O clique em **Entrar** deve inverter esse estado. Se o botão apontar para a ação errada ou se os dois formulários ficarem visíveis ao mesmo tempo, uma das assertions falha.

## 8. Uso de inteligência artificial

- **Ferramenta:** Codex.
- **Uso:** apoio à escolha do fluxo, implementação da regra e dos testes, execução e organização do Markdown.
- **Sugestão alterada:** a proposta inicial de automatizar a busca de restaurantes pela página inicial foi substituída pela alternância dos formulários. Sem sessão autenticada, o endereço abre a tela de entrada.
- **Verificação:** a interface foi inspecionada no navegador. As falhas esperadas durante o TDD foram reproduzidas, e o pytest executou os quatro testes, incluindo o fluxo no Chromium contra o site publicado.

## 9. Diferenciais implementados

- Terceiro teste unitário para o valor imediatamente abaixo do mínimo (TU03).
- Uso de `pytest.raises` para verificar a exceção de valor negativo (TU02).

[Ver os testes unitários](test_regras_localeats.py).
