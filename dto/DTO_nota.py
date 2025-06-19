def nota_to_dict(nota):
    base = {
        "id": nota.get_id_nota(),
        "valor_nota": nota.get_valor_nota(),
        "id_materia": nota.get_id_materia(),
    }
    if hasattr(nota, "get_valor_recuperatorio"):
        base["recuperatorio"] = nota.get_valor_recuperatorio()
    return base
