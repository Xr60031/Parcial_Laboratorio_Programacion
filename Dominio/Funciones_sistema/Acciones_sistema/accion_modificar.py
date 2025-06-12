from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar_parcial import Modificar_Parcial
from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar_atributo import Modificar_Atributo
from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar

class Modificar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.ATRIBUTOS_DISPONIBLES = [
            "nombre_materia",
            "nombre_docente",
            "nota_min_aprobar",
            "es_promocionable",
            "nota_min_promocion",
            "cant_veces_final_rendible",
            "cant_parciales"
        ]

    def modificar_parcial(self):
        notas = self.main.persistencia.obtener_parciales(self.materia_seleccionada)

        self.main.cli.mostrar_datos([
            "ID", "VAL", "REC"
        ])

        for nota in notas:
            self.main.cli.mostrar_datos([
                nota.id_nota, nota.valor_nota, nota.valor_recuperatorio
            ])

        id_nota = self.main.cli.obtener_dato(
            "ID del parcial a modificar: "
        )

        self.main.accion = Modificar_Parcial(self.main, self.materia_seleccionada, id_nota)

    def cambiar_a_modificar_atributo(self, atributo):
        self.main.accion = Modificar_Atributo(atributo)

    def volver(self):
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        self.main.cli.mostrar_datos([
            "Estos son los atributos disponibles:"
        ])

        for i in range(len(self.ATRIBUTOS_DISPONIBLES)):
            self.main.cli.mostrar_datos([
                i+1, self.ATRIBUTOS_DISPONIBLES[i]
            ])
        
        self.main.cli.mostrar_datos([
            "P", "parcial"
        ])

        self.main.cli.mostrar_datos([
            "F", "final"
        ])

        accion_elegida = self.main.cli.obtener_dato(
            "Atributo a modificar (X = Volver): "
        )
        
        if accion_elegida.upper() == "P":
            self.modificar_parcial()
        elif accion_elegida.upper() == "X":
            self.volver()
        else:
            self.cambiar_a_modificar_atributo(accion_elegida)
