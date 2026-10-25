def validar_item(item: dict) -> None:
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total


def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
    if total_pedido >= 100:
        return 0

    distancia_excedente = max(distancia_km - 3, 0)
    return 5 + distancia_excedente * 2
