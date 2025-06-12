from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Materias.parcial import Parcial

class Agregar_Parcial(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_parcial(self, valor):
        parcial = Parcial((None, self.materia_seleccionada.id_materia, valor))
        self.main.persistencia.agregar_parcial(parcial)
        self.main.cli.mostrar_datos([
            "Parcial agregado."
        ])
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar_nota import Agregar_Nota
        self.main.accion = Agregar_Nota(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.cli.obtener_dato(
            "Nota del parcial (X = Volver)"
        )

        if valor.upper() != "X":
            self.agregar_parcial(valor)
        else:
            self.volver()