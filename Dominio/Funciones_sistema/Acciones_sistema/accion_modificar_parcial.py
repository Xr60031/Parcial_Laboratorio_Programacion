from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Parcial(Accion):
    def __init__(self, main, materia, id_nota):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.parcial_seleccionado = id_nota
        self.acciones_disponibles = {
            "V": self.valor_nota_seleccionado,
            "R": self.valor_recuperatorio_seleccionado,
            "X": self.volver
        }

    def valor_nota_seleccionado(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar_valor_nota import Modificar_Valor_Nota
        self.main.accion = Modificar_Valor_Nota(self.main, self.materia_seleccionada, self.parcial_seleccionado)

    def valor_recuperatorio_seleccionado(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar_valor_recuperatorio import Modificar_Valor_Recuperatorio
        self.main.accion = Modificar_Valor_Recuperatorio(self.main, self.materia_seleccionada, self.parcial_seleccionado)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar import Modificar
        self.main.accion = Modificar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        accion_elegida = self.main.cli.obtener_dato(
            "Nota a modificar (V = Nota original, R = Nota del recuperatorio, X = Volver)"
        )
        self.acciones_disponibles[accion_elegida.upper()]()
