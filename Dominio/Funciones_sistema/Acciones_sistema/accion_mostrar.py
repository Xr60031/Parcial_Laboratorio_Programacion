import sys
from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Funciones_sistema.Acciones_sistema.accion_borrar_base import Borrar_Base

class Mostrar(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.ACCIONES_DISPONIBLES = {
            "A": self.cambiar_a_agregar,
            "B": self.cambiar_a_borrar_base,
            "X": self.salir
        }
    
    def cambiar_a_agregar(self):
        self.main.accion = Agregar(self.main)

    def cambiar_a_borrar_base(self):
        self.main.accion = Borrar_Base(self.main)

    def cambiar_a_seleccionar(self, id_materia_elegida, materias):
        self.main.accion = Seleccionar(self.main, materias[id_materia_elegida]) #not really

    def salir(self):
        sys.exit(0)

    def hacer_accion(self):
        materias = self.main.persistencia.obtener_materias()
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

        resultado = self.main.cli.obtener_dato(
            "Acción (A = Agregar, B = Borrar base, [cod_materia] = Seleccionar, X = Salir): "
        )

        if type(resultado) == int:
            self.cambiar_a_seleccionar(resultado, materias)
        else:
            self.ACCIONES_DISPONIBLES[resultado.upper()]()

