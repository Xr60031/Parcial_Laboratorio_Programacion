from Handlers.nota_handler import NotaHandler


class RecuperatorioHandler(NotaHandler):
    def agregar(self, id_nota, valor_recuperatorio, persistencia):
        persistencia.agregar_recuperatorio(id_nota, valor_recuperatorio)
