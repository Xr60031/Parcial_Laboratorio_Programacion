from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Funciones_sistema.Calculos_notas.Sin_Criterio.promedio import Promedio

class Seleccionar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.ACCIONES_DISPONIBLES = {
            "N": self.cambiar_a_agregar_nota,
            "M": self.cambiar_a_modificar,
            "E": self.cambiar_a_eliminar,
            "X": self.volver
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
            if materia.id_materia == int(id_materia):
                return materia
        return None

    def hacer_accion(self):
        materias = self.main.persistencia.obtener_materias()

        self.materia_seleccionada = self.buscar_materia(self.materia_seleccionada.id_materia, materias)

        self.main.cli.mostrar_datos([
            "-------------------------------------------------"
        ])

        self.main.cli.mostrar_datos([
            f"ID: {self.materia_seleccionada.id_materia}"
        ])

        self.main.cli.mostrar_datos([
            f"Materia: {self.materia_seleccionada.nombre_materia}"
        ])

        self.main.cli.mostrar_datos([
            f"Docente: {self.materia_seleccionada.nombre_docente}"
        ])

        self.main.cli.mostrar_datos([
            f"Nota minima para Aprobar: {self.materia_seleccionada.nota_min_aprobar}"
        ])

        if self.materia_seleccionada.es_promocionable:
            self.main.cli.mostrar_datos([
                f"Nota minima para Promocionar: {self.materia_seleccionada.nota_min_promocion}"
            ])

        self.main.cli.mostrar_datos([
            f"Cantidad de oportunidades de final: {self.materia_seleccionada.cant_veces_final_rendible}"
        ])

        self.main.cli.mostrar_datos([
            f"Cantidad de Parciales: {self.materia_seleccionada.cant_parciales}"
        ])

        parciales = self.main.persistencia.obtener_parciales(self.materia_seleccionada)

        if len(parciales) > 0:
            self.main.cli.mostrar_datos([
                "PARCIAL", "RECUPERATORIO"
            ])

            for parcial in parciales:
                valores = [parcial.valor_nota]
                if parcial.valor_recuperatorio:
                    valores.append(parcial.valor_recuperatorio)
                self.main.cli.mostrar_datos(valores)
        else:
            self.main.cli.mostrar_datos([
                "No hay parciales registrados de esta materia."
            ])

        finales = self.main.persistencia.obtener_finales(self.materia_seleccionada)

        if len(finales) > 0:
            self.main.cli.mostrar_datos([
                "FINALES"
            ])

            for final in finales:
                self.main.cli.mostrar_datos([
                    final.valor_nota
                ])
        else:
            self.main.cli.mostrar_datos([
                "No hay finales registrados de esta materia."
            ])

        self.main.builder_determinador.construir()
        determinador = self.main.builder_determinador.get_resultado()
        self.main.builder_determinador.reset()

        estado_materia = determinador.consultar_estado(parciales, finales, self.materia_seleccionada)

        self.main.cli.mostrar_datos([
            f"ESTADO: {estado_materia.name}"
        ])

        if estado_materia == Estado.REGULARIZADO:
            indicador = Indicador_Cantidad_Finales_Restantes(Intentos_Final_Restante())
            self.main.cli.mostrar_datos([
                f"Oportunidades de final restantes: {indicador.cantidad_finales_restante(finales, self.materia_seleccionada)}"
            ])
        elif estado_materia == Estado.APROBADO:
            self.main.cli.mostrar_datos([
                f"Nota final de la materia: {finales[-1].valor_nota}"
            ])
        elif estado_materia == Estado.APROBADO:
            promedio = Promedio()
            self.main.cli.mostrar_datos([
                f"Nota final de la materia: {promedio.operacion(parciales)}"
            ])
        
        self.main.cli.mostrar_datos([
            "-------------------------------------------------"
        ])

        accion_elegida = self.main.cli.obtener_dato(
            "Acción (N = Agregar nota, M = Modificar materia, E = Eliminar materia, X = Volver)"
        )
        self.ACCIONES_DISPONIBLES[accion_elegida.upper()]()
