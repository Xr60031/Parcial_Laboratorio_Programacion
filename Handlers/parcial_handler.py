from Handlers.nota_handler import NotaHandler


class ParcialHandler(NotaHandler):
    def agregar(self, id_materia, nota_valor, persistencia):
        from Dominio.Materias.parcial import Parcial
        parcial = Parcial([None, id_materia, nota_valor, None])
        persistencia.agregar_parcial(parcial)

