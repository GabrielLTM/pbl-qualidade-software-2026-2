from src.pedido import calcular_taxa_entrega


def test_cobra_cinco_reais_para_dois_km_e_pedido_de_cinquenta_reais():
    assert calcular_taxa_entrega(2, 50) == 5


def test_cobra_sete_reais_para_quatro_km_e_pedido_de_cinquenta_reais():
    assert calcular_taxa_entrega(4, 50) == 7


def test_entrega_gratuita_para_cinco_km_e_pedido_de_cem_reais():
    assert calcular_taxa_entrega(5, 100) == 0
