class MateriaController:
    def __init__(self, persistencia, determinador, nota_handlers: dict):
        self.persistencia = persistencia
        self.determinador = determinador
        self.handlers = nota_handlers

    def crear_materia(self, materia):
        self.persistencia.agregar_materia(materia)
        return materia

    def eliminar_materia(self, id_materia):
        self.persistencia.eliminar_materia(id_materia)

    def agregar_nota(self, id_materia, tipo, nota):
        if tipo not in self.handlers:
            raise ValueError("Tipo de nota no soportado")
        self.handlers[tipo].agregar(id_materia, nota, self.persistencia)

    def obtener_materia_con_estado(self, id_materia):
        materias = []
        for m in self.persistencia.obtener_materias():
            if m.get_id_materia() == id_materia:
                materias.append(m)

        if not materias:
            raise ValueError("Materia no encontrada")
        materia = materias[0]
        parciales = self.persistencia.obtener_parciales(materia)
        finales = self.persistencia.obtener_finales(materia)
        from Dominio.Materias.datos import Datos
        datos = Datos(materia, parciales, finales)
        estado = self.determinador.consultar_estado(datos)
        return materia, parciales, finales, estado