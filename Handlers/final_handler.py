from Handlers.nota_handler import NotaHandler


class FinalHandler(NotaHandler):
    def agregar(self, id_materia, nota_valor, persistencia):
        from Dominio.Materias.final import Final
        final = Final([None, id_materia, nota_valor])
        persistencia.agregar_final(final)
