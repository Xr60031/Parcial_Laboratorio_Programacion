from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

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
        from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar_nota import Agregar_Nota
        self.main.accion = Agregar_Nota(self.main, self.materia_seleccionada)

    def cambiar_a_modificar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar import Modificar
        self.main.accion = Modificar(self.main, self.materia_seleccionada)

    def cambiar_a_eliminar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_eliminar import Eliminar
        self.main.accion = Eliminar(self.main, self.materia_seleccionada)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar
        self.main.accion = Mostrar(self.main)

    def hacer_accion(self):

        self.main.cli.mostrar_datos()

        accion_elegida = self.main.cli.obtener_dato(
            "Acción (N = Agregar nota, M = Modificar materia, E = Eliminar materia, X = Volver)"
        )
        self.ACCIONES_DISPONIBLES[accion_elegida.upper()]()
