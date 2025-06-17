from Manejo_consola.interfaces.input import Interfaz_Input
from Manejo_consola.interfaces.output import Interfaz_Output
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Cantidad_Finales_Menor_Max import Cantidad_Finales_Menor_Max
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Funciones_sistema.Calculos_notas.promedio import Promedio
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado
from Dominio.Materias.datos import Datos
from Dominio.Materias.materia import Materia

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
    
    def mostrar_tabla(self, materias: list[Materia], persistencia, builder_determinador):
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
                determinador: Determinador_Estado = builder_determinador.get_resultado()
                builder_determinador.reset()

                estado_materia = determinador.consultar_estado(Datos(materia, parciales, finales))

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
                nota.get_id_nota() if id else "",
                nota.get_valor_nota(),
                nota.get_valor_recuperatorio() if recu and nota.get_valor_recuperatorio() else "",
                sep="\t"
            )

    def mostrar_info_materia(self, materia_seleccionada: Materia, persistencia, builder_determinador):
        print("-------------------------------------------------")

        print(f"ID: {materia_seleccionada.get_id_materia()}")

        print(f"Materia: {materia_seleccionada.get_nombre_materia()}")

        print(f"Docente: {materia_seleccionada.get_nombre_docente()}")

        print(f"Nota minima para Aprobar: {materia_seleccionada.get_nota_min_aprobar()}")

        print(f"¿Es promocionable?: {"Sí" if materia_seleccionada.get_es_promocionable() else "No"}")
        
        if materia_seleccionada.get_es_promocionable():
            print(f"Nota minima para Promocionar: {materia_seleccionada.get_nota_min_promocion()}")

        print(f"Cantidad de oportunidades de final: {materia_seleccionada.get_cant_veces_final_rendible()}")

        print(f"Cantidad de Parciales: {materia_seleccionada.get_cant_parciales()}")

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
        determinador: Determinador_Estado = builder_determinador.get_resultado()
        builder_determinador.reset()

        estado_materia = determinador.consultar_estado(Datos(materia_seleccionada, parciales, finales))

        print(f"ESTADO: {estado_materia.name}")

        if estado_materia == Estado.REGULARIZADO:
            indicador = Indicador_Cantidad_Finales_Restantes(Cantidad_Finales_Menor_Max())
            print(f"Oportunidades de final restantes: {indicador.cantidad_finales_restante(finales, materia_seleccionada)}")
        elif estado_materia == Estado.APROBADO:
            print(f"Nota final de la materia: {finales[-1].valor_nota}")
        elif estado_materia == Estado.PROMOCIONADO:
            promedio = Promedio()
            print(f"Nota final de la materia: {promedio.promediar(parciales)}")
        
        print("-------------------------------------------------")