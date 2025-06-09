from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante

class Indicador_Cantidad_Finales_Restantes():
    def __init__(self):
        self.intentos_final = Intentos_Final_Restante()

    def cantidad_finales_restante(self, notas_parciales, materia):
        return self.intentos_final.operacion(notas_parciales, materia.cant_veces_final_rendible)