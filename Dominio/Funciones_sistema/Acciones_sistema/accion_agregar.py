from Dominio.Materias.materia import Materia
from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Agregar(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.DATOS = [
            "Código de la materia",
            "Nombre de la materia",
            "Nombre completo del docente",
            "Nota mínima necesaria para aprobar un parcial/final",
            "¿Es promocionable la materia? (True/False)",
            "Nota mínima necesaria para promocionar un parcial",
            "¿Cuántas veces podés intentar rendir el final antes de recursar?",
            "Cantidad de parciales"
        ]
    
    def cambiar_a_mostrar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar
        self.main.accion = Mostrar(self.main)

    def hacer_accion(self):
        self.main.cli.mostrar_datos([
            "Ingrese los datos a medida que se piden (X = Volver)"
        ])

        datos = tuple()
        
        for i in range(len(self.DATOS)):
            respuesta = self.main.cli.obtener_dato(
                self.DATOS[i] + ": "
            )

            if respuesta.upper() != "X":
                datos[i] = respuesta
            else:
                self.cambiar_a_mostrar()
        
        nueva_materia = Materia(datos)

        self.main.cli.agregar_materia(nueva_materia)

        self.main.cli.mostrar_datos([
            "¡Materia Agregada!"
        ])

        self.cambiar_a_mostrar()