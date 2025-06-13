from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Seleccionar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.ACCIONES_DISPONIBLES = {
            "A": (self.cambiar_a_agregar_nota, "Agregar nota"),
            "M": (self.cambiar_a_modificar, "Modificar materia"),
            "E": (self.cambiar_a_eliminar, "Eliminar materia"),
            "X": (self.volver, "Volver")
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
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)

    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.id_materia == id_materia:
                return materia
        return None

    def hacer_accion(self):
        materias = self.main.persistencia.obtener_materias()

        self.materia_seleccionada = self.buscar_materia(self.materia_seleccionada.id_materia, materias)

        self.main.interfaz_salida.mostrar_info_materia(self.materia_seleccionada, self.main.persistencia, self.main.builder_determinador)

        opcion_elegida = self.main.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
