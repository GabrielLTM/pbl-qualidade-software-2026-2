import pytest

from regras_localeats import pedido_atingiu_valor_minimo


# Responsável: Gabriel Lessa Tramasol Machado
def test_pedido_de_trinta_reais_atinge_o_minimo():
    assert pedido_atingiu_valor_minimo(30) is True


# Responsável: Gabriel Lessa Tramasol Machado
def test_pedido_com_valor_negativo_gera_erro():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-0.01)


# Responsável: Gabriel Lessa Tramasol Machado
def test_pedido_de_um_centavo_abaixo_do_minimo_nao_atinge_o_minimo():
    assert pedido_atingiu_valor_minimo(29.99) is False
