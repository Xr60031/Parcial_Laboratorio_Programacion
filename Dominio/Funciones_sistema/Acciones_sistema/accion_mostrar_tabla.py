import sys
from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Mostrar_Tabla(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.ACCIONES_DISPONIBLES = {
            "A": self.cambiar_a_agregar,
            "B": self.cambiar_a_borrar_base,
            "X": self.salir
        }
    
    def cambiar_a_agregar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar import Agregar
        self.main.accion = Agregar(self.main)

    def cambiar_a_borrar_base(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_borrar_base import Borrar_Base
        self.main.accion = Borrar_Base(self.main)
    
    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.id_materia == int(id_materia):
                return materia
        return None

    def cambiar_a_seleccionar(self, id_materia_elegida, materias):
        materia_seleccionada = self.buscar_materia(id_materia_elegida, materias)
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, materia_seleccionada)

    def salir(self):
        sys.exit(0)

    def hacer_accion(self):
        materias = self.main.persistencia.obtener_materias()
        if len(materias) > 0:
            self.main.cli.mostrar_datos([
                "-------------------------------------------------"
            ])

            self.main.cli.mostrar_datos([
                "ID",
                "Nombre",
                "Estado"
            ])

            for materia in materias:
                parciales = self.main.persistencia.obtener_parciales(materia)
                finales = self.main.persistencia.obtener_finales(materia)

                self.main.builder_determinador.construir()
                determinador = self.main.builder_determinador.get_resultado()
                self.main.builder_determinador.reset()

                estado_materia = determinador.consultar_estado(parciales, finales, materia)

                self.main.cli.mostrar_datos([
                    materia.get_id_materia(),
                    materia.get_nombre_materia(),
                    estado_materia.name
                ])
            
            self.main.cli.mostrar_datos([
                "-------------------------------------------------"
            ])
        else:
            self.main.cli.mostrar_datos([
                "No hay materias registradas."
            ])

        resultado = self.main.cli.obtener_dato(
            "Acción (A = Agregar, B = Borrar base, [ID] = Seleccionar, X = Salir)"
        )

        if resultado.upper() in self.ACCIONES_DISPONIBLES:
            self.ACCIONES_DISPONIBLES[resultado.upper()]()
        else:
            self.cambiar_a_seleccionar(resultado, materias)
