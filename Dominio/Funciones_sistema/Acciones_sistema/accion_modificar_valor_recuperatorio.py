from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Valor_Recuperatorio(Accion):
    def __init__(self, main, materia, id_nota):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.id_nota = id_nota

    def cambiar_a_seleccionar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.interfaz_entrada.obtener_decimal("Nota del recuperatorio")
        self.main.persistencia.modificar_parcial(self.id_nota, "valor_recuperatorio", valor)
        self.cambiar_a_seleccionar()