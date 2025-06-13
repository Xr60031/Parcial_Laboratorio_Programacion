from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Materias.parcial import Parcial

class Agregar_Parcial(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_parcial(self, valor):
        parcial = Parcial((None, self.materia_seleccionada.id_materia, valor))
        self.main.persistencia.agregar_parcial(parcial)
        self.main.interfaz_salida.mostrar_advertencia("parcial_agregado")

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.interfaz_entrada.obtener_decimal("Nota del parcial")
        self.agregar_parcial(valor)
        self.volver()