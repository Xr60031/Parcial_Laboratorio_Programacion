from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Agregar_Recuperatorio(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_recuperatorio(self, id_nota, valor):
        self.main.persistencia.modificar_parcial(id_nota, "valor_recuperatorio", valor)
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def volver(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_agregar_nota import Agregar_Nota
        self.main.accion = Agregar_Nota(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        notas = self.main.persistencia.obtener_parciales(self.materia_seleccionada)

        self.main.cli.mostrar_datos([
            "ID", "VAL"
        ])

        for nota in notas:
            if not nota.valor_recuperatorio:
                self.main.cli.mostrar_datos([
                    nota.id_nota, nota.valor_nota
                ])

        id_nota = self.main.cli.obtener_dato(
            "ID del parcial a agregar recuperatorio"
        )
        
        valor = self.main.cli.obtener_dato(
            "Nota del parcial (X = Volver)"
        )

        if valor.upper() != "X":
            self.agregar_recuperatorio(id_nota, valor)
        else:
            self.volver()