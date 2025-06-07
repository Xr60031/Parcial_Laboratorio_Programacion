from accion import Accion

class Mostrar(Accion):
    def __init__(self):
        super().__init__()

    def hacer_accion(self, main):
        materias = main.persistencia.obtener_materias()
        for materia in materias:
            parciales = main.persistencia.obtener_parciales(materia)
            finales = main.persistencia.obtener_finales(materia)

            main.builder_determinador.construir()
            determinador = main.builder_determinador.get_resultado()
            main.builder_determinador.reset()

            estado_materia = determinador.consultar_estado(parciales, finales, materia)

            main.cli.mostrar_datos([
                materia.get_id_materia(),
                materia.get_nombre_materia(),
                estado_materia.name
            ]
            )

            main.cli.obtener_dato(
                "Accion (Agregar, Eliminar, Mas informacion): "
            )