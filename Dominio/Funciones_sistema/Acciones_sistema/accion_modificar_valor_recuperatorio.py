from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Valor_Recuperatorio(Accion):
    def __init__(self, main, materia, id_nota):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.id_nota = id_nota

    def cambiar_a_seleccionar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar_parcial import Modificar_Parcial
        self.main.accion = Modificar_Parcial(self.main, self.materia_seleccionada, self.id_nota)

    def hacer_accion(self):
        valor = self.main.cli.obtener_dato("Nota del recuperatorio (X = Volver)")
        if valor.upper() != "X":
            self.main.persistencia.modificar_parcial(self.id_nota, "valor_recuperatorio", valor)
            self.cambiar_a_seleccionar()
        else:
            self.volver()