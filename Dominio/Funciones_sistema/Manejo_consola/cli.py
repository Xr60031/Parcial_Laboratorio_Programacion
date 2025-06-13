from Dominio.Funciones_sistema.Manejo_consola.interfaces.input import Interfaz_Input
from Dominio.Funciones_sistema.Manejo_consola.interfaces.output import Interfaz_Output
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Funciones_sistema.Calculos_notas.Sin_Criterio.promedio import Promedio

class CLI(Interfaz_Input, Interfaz_Output):
    def __init__(self):
        super().__init__()

    def obtener_entero(self, entero_a_obtener):
        while True:
            ingreso = input(f'Ingrese {entero_a_obtener}: ')
            try:
                ingreso = int(ingreso)
                return ingreso
            except Exception:
                self.mostrar_advertencia("no_entero")
    
    def obtener_decimal(self, decimal_a_obtener):
        while True:
            ingreso = input(f'Ingrese {decimal_a_obtener}: ')
            try:
                ingreso = float(ingreso)
                return ingreso
            except Exception:
                self.mostrar_advertencia("no_decimal")

    def obtener_cadena(self, cadena_a_obtener):
        ingreso = input(f'Ingrese {cadena_a_obtener}: ')
        return ingreso

    def obtener_booleano(self, booleano_a_obtener):
        while True:
            ingreso = input(f'{booleano_a_obtener} (S/N): ').upper()
            if ingreso == "S":
                return True
            elif ingreso == "N":
                return False
            else:
                self.mostrar_advertencia("no_booleano")
    
    def seleccionar_opcion(self, opciones_disponibles):
        print("\t-- Opciones disponibles --")
        for opcion in opciones_disponibles:
            print(f"\t{opcion} => {opciones_disponibles[opcion][1]}")
        while True:
            opcion_elegida = input("Ingrese Opción: ").upper()
            if opcion_elegida in opciones_disponibles:
                return opciones_disponibles[opcion_elegida]
            else:
                self.mostrar_advertencia("opcion_invalida")
    
    def mostrar_advertencia(self, id_advertencia):
        print(self.ADVERTENCIAS[id_advertencia])
    
    def mostrar_tabla(self, materias, persistencia, builder_determinador):
        print("-------------------------------------------------")
        if len(materias) > 0:
            print(
                "ID",
                "Estado\t",
                "Materia",
                sep="\t"
            )

            for materia in materias:
                parciales = persistencia.obtener_parciales(materia)
                finales = persistencia.obtener_finales(materia)

                builder_determinador.construir()
                determinador = builder_determinador.get_resultado()
                builder_determinador.reset()

                estado_materia = determinador.consultar_estado(parciales, finales, materia)

                print(
                    materia.get_id_materia(),
                    estado_materia.name,
                    materia.get_nombre_materia(),
                    sep="\t"
                )
        else:
            print("No hay materias registradas.")
        print("-------------------------------------------------")
    
    def mostrar_notas(self, notas, recu=False, id=False):
        print(
            "ID" if id else "",
            "Nota",
            "Recuperatorio" if recu else "",
            sep="\t"
        )

        for nota in notas:
            print(
                nota.id_nota if id else "",
                nota.valor_nota,
                nota.valor_recuperatorio if recu and nota.valor_recuperatorio else "",
                sep="\t"
            )

    def mostrar_info_materia(self, materia_seleccionada, persistencia, builder_determinador):
        print("-------------------------------------------------")

        print(f"ID: {materia_seleccionada.id_materia}")

        print(f"Materia: {materia_seleccionada.nombre_materia}")

        print(f"Docente: {materia_seleccionada.nombre_docente}")

        print(f"Nota minima para Aprobar: {materia_seleccionada.nota_min_aprobar}")

        print(f"¿Es promocionable?: {"Sí" if materia_seleccionada.es_promocionable else "No"}")
        
        if materia_seleccionada.es_promocionable:
            print(f"Nota minima para Promocionar: {materia_seleccionada.nota_min_promocion}")

        print(f"Cantidad de oportunidades de final: {materia_seleccionada.cant_veces_final_rendible}")

        print(f"Cantidad de Parciales: {materia_seleccionada.cant_parciales}")

        parciales = persistencia.obtener_parciales(materia_seleccionada)

        if len(parciales) > 0:
            print("\t-- PARCIALES --")
            self.mostrar_notas(parciales, recu=True)
        else:
            print("No hay parciales registrados de esta materia.")

        finales = persistencia.obtener_finales(materia_seleccionada)

        if len(finales) > 0:
            print("\t-- FINALES --")
            self.mostrar_notas(finales)
        else:
            print("No hay finales registrados de esta materia.")

        print("----------")

        builder_determinador.construir()
        determinador = builder_determinador.get_resultado()
        builder_determinador.reset()

        estado_materia = determinador.consultar_estado(parciales, finales, materia_seleccionada)

        print(f"ESTADO: {estado_materia.name}")

        if estado_materia == Estado.REGULARIZADO:
            indicador = Indicador_Cantidad_Finales_Restantes(Intentos_Final_Restante())
            print(f"Oportunidades de final restantes: {indicador.cantidad_finales_restante(finales, materia_seleccionada)}")
        elif estado_materia == Estado.APROBADO:
            print(f"Nota final de la materia: {finales[-1].valor_nota}")
        elif estado_materia == Estado.PROMOCIONADO:
            promedio = Promedio()
            print(f"Nota final de la materia: {promedio.operacion(parciales)}")
        
        print("-------------------------------------------------")