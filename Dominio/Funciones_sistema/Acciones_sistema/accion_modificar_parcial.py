from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Parcial(Accion):
    def __init__(self, main, id_materia, id_nota):
        super().__init__(main)
        self.id_materia_seleccionada = id_materia
        self.id_parcial_seleccionado = id_nota
        self.acciones_disponibles = {
            "V": self.valor_nota_seleccionado,
            "R": self.valor_recuperatorio_seleccionado,
            "X": self.volver
        }

    def valor_nota_seleccionado(self):
        self.main.accion = ValorNotaSeleccionado(self.main, self.id_materia_seleccionada, self.id_parcial_seleccionado)

    def valor_recuperatorio_seleccionado(self):
        self.main.accion = ValorRecuperatorioSeleccionado(self.main, self.id_materia_seleccionada, self.id_parcial_seleccionado)

    def volver(self):
        self.main.accion = Modificar(self.main, self.id_materia_seleccionada)

    def hacer_accion(self):
        accion_elegida = self.main.cli.obtener_dato(
            "Nota a modificar (V = Nota original, R = Nota del recuperatorio, X = Volver): "
        )
        self.acciones_disponibles[accion_elegida.upper()]()
