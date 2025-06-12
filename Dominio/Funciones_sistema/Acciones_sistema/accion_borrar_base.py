from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Borrar_Base(Accion):
    def __init__(self, main):
        super().__init__(main)
    
    def cambiar_a_mostrar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)
        

    def hacer_accion(self):
        self.main.cli.mostrar_datos([
            "¿Estás seguro que querés borrar toda la información de materias y notas de la base?"
        ])
        respuesta = self.main.cli.obtener_dato(
            "Confirmación (S = Sí, X = No)"
        )

        if respuesta.upper() == "S":
            self.main.persistencia.eliminar_base()
            self.main.cli.mostrar_datos([
                "Base borrada."
            ])
        
        self.cambiar_a_mostrar()