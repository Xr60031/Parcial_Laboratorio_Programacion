from flask import Blueprint, request, jsonify
from Dominio.Materias.materia import Materia
from dto.DTO_materia import materia_con_estado_to_dict, materia_to_dict

def crear_rutas(controller):
    bp = Blueprint("materias", __name__)

    @bp.route("/materias", methods=["POST"])
    def crear_materia():
        data = request.get_json()
        materia = Materia([
            data.get("id"),
            data.get("nombre"),
            data.get("docente"),
            data.get("nota_min_aprobar"),
            data.get("es_promocionable"),
            data.get("nota_min_promocion"),
            data.get("cant_veces_final_rendible"),
            data.get("cant_parciales")
        ])
        controller.crear_materia(materia)
        return jsonify(materia_to_dict(materia)), 201

    @bp.route("/materias/<int:id_materia>", methods=["DELETE"])
    def eliminar_materia(id_materia):
        controller.eliminar_materia(id_materia)
        return "", 204

    @bp.route("/materias/<int:id_materia>/notas", methods=["POST"])
    def agregar_nota(id_materia):
        data = request.get_json()
        tipo = data.get("tipo")
        nota = float(data.get("nota"))
        controller.agregar_nota(id_materia, tipo, nota)
        return "", 204

    @bp.route("/materias/<int:id_materia>", methods=["GET"])
    def consultar_estado(id_materia):
        try:
            materia, parciales, finales, estado = controller.obtener_materia_con_estado(id_materia)
            return jsonify(materia_con_estado_to_dict(materia, parciales, finales, estado))
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    return bp