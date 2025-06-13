from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Agregar_Recuperatorio(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_recuperatorio(self, id_nota, valor):
        self.main.persistencia.agregar_recuperatorio(id_nota, valor)
        self.main.interfaz_salida.mostrar_advertencia("recuperatorio_agregado")

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        parciales = self.main.persistencia.obtener_parciales(self.materia_seleccionada)

        if len(parciales) > 0:
            self.main.interfaz_salida.mostrar_notas(parciales, recu=True, id=True)
            id_nota = self.main.interfaz_entrada.obtener_entero("ID del parcial a agregar/sobreescribir recuperatorio")
            valor = self.main.interfaz_entrada.obtener_decimal("Nota del recuperatorio")
            self.agregar_recuperatorio(id_nota, valor)
        else:
            self.main.interfaz_salida.mostrar_advertencia("sin_notas")
        self.volver()