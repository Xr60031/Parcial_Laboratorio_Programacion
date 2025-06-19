from dto.DTO_nota import nota_to_dict

def materia_to_dict(materia):
    return {
        "id": materia.get_id_materia(),
        "nombre": materia.get_nombre_materia(),
        "docente": materia.get_nombre_docente(),
        "nota_min_aprobar": materia.get_nota_min_aprobar(),
        "es_promocionable": materia.get_es_promocionable(),
        "nota_min_promocion": materia.get_nota_min_promocion(),
        "cant_veces_final_rendible": materia.get_cant_veces_final_rendible(),
        "cant_parciales": materia.get_cant_parciales(),
    }

def materia_con_estado_to_dict(materia, parciales, finales, estado):
    return {
        **materia_to_dict(materia),
        "parciales": [nota_to_dict(p) for p in parciales],
        "finales": [nota_to_dict(f) for f in finales],
        "estado": estado.name
    }