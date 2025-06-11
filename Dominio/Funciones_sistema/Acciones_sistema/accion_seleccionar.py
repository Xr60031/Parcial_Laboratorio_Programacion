from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar
from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar_nota import Agregar_Nota

class Seleccionar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.ACCIONES_DISPONIBLES = {
            "N": self.cambiar_a_agregar_nota,
            "M": self.cambiar_a_modificar,
            "E": self.cambiar_a_eliminar,
            "X": self.volver
        }

    def cambiar_a_agregar_nota(self):
        self.main.accion = Agregar_Nota(self.main, self.materia_seleccionada)

    def cambiar_a_modificar(self):
        self.main.accion = Modificar(self.main, self.materia_seleccionada)

    def cambiar_a_eliminar(self):
        self.main.accion = Eliminar(self.main, self.materia_seleccionada)

    def volver(self):
        self.main.accion = Mostrar(self.main)

    def hacer_accion(self):

        self.main.cli.mostrar_datos()

        accion_elegida = self.main.cli.obtener_dato(
            "Acción (N = Agregar nota, M = Modificar materia, E = Eliminar materia, X = Volver): "
        )
        self.ACCIONES_DISPONIBLES[accion_elegida.upper()]()
