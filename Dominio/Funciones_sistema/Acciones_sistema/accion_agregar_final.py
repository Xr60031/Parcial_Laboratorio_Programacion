from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Materias.final import Final

class Agregar_Final(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_final(self, valor):
        final = Final((None, self.materia_seleccionada.get_id_materia(), valor))
        self.main.persistencia.agregar_final(final)
        self.main.interfaz_salida.mostrar_advertencia("final_agregado")

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.interfaz_entrada.obtener_decimal("Nota del final")
        self.agregar_final(valor)
        self.volver()