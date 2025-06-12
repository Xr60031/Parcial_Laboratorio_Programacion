from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Eliminar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
    
    def volver(self, id_materia_elegida, materias):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, materias[id_materia_elegida])

    def eliminar_y_mostrar_tabla(self, ID_materia_seleccionada):
        self.main.persistencia.eliminar_parcial(ID_materia_seleccionada)
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar
        self.main.accion = Mostrar(self.main)

    def hacer_accion(self):
        self.main.cli.mostrar_datos([
            f"¿Estás seguro que querés eliminar la materia {self.materia_seleccionada.nombre_materia}?"
        ])
        accion_elegida = self.main.cli.obtener_dato(
            "Confirmación (S = Sí, X = No)"
        )

        if accion_elegida.upper() == "S":
            self.eliminar_y_mostrar_tabla(self.materia_seleccionada.id_materia)
        else:
            self.volver()
