from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Agregar_Nota(Accion):
    def __init__(self, main, id_materia):
        super().__init__(main)
        self.id_materia_seleccionada = id_materia
        self.ACCIONES_DISPONIBLES = {
            "P": self.agregar_parcial,
            "F": self.agregar_final,
            "R": self.agregar_recuperatorio,
            "X": self.volver
        }

    def agregar_parcial(self):
        self.main.accion = Agregar_Parcial(self.main, self.id_materia_seleccionada)

    def agregar_final(self):
        self.main.accion = Agregar_Final(self.main, self.id_materia_seleccionada)

    def agregar_recuperatorio(self):
        self.main.accion = Agregar_Recuperatorio(self.main, self.id_materia_seleccionada)

    def volver(self):
        self.main.accion = Seleccionar(self.main, self.id_materia_seleccionada)

    def hacer_accion(self):
        accion_elegida = self.main.cli.obtener_dato(
            "Tipo de Nota (P = Agregar parcial, F = Agregar final, R = Agregar recuperatorio, X = Volver): "
        )
        self.ACCIONES_DISPONIBLES[accion_elegida.upper()]()
