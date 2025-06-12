from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Atributo(Accion):
    def __init__(self, main, materia, atributo):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.atributo = atributo

    def cambiar_a_seleccionar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def modificar_final(self):
        notas = self.main.persistencia.obtener_finales(self.materia_seleccionada)

        self.main.cli.mostrar_datos([
            "ID", "VAL"
        ])

        for nota in notas:
            self.main.cli.mostrar_datos([
                nota.id_nota, nota.valor_nota
            ])

        id_nota = self.main.cli.obtener_dato(
            "ID del final a modificar: "
        )

        valor = self.main.cli.obtener_dato(
            "Nota del final: "
        )

        self.main.persistencia.modificar_final(id_nota, "valor_nota", valor)

    def modificar_atributo(self):
        valor = self.main.cli.obtener_dato(
            "Nuevo valor: "
        )

        self.main.persistencia.modificar_materia(self.materia_seleccionada.id_materia, self.atributo, valor)
    
    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_modificar import Modificar
        self.main.accion = Modificar(self.main, self.materia_seleccionada)

    def realizar_accion(self):
        if self.atributo.upper() == "F":
            self.modificar_final()
        else:
            self.modificar_atributo()
        
        self.cambiar_a_seleccionar()