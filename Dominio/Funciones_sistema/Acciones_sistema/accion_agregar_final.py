from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Materias.final import Final

class Agregar_Final(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_final(self, valor):
        final = Final(None, self.materia_seleccionada.id_materia, valor)
        self.main.persistencia.agregar_final(final)
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar_nota import Agregar_Nota
        self.main.accion = Agregar_Nota(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.cli.obtener_dato(
            "Nota del final (X = Volver): "
        )

        if valor.upper() != "X":
            self.agregar_final(valor)
        else:
            self.volver()