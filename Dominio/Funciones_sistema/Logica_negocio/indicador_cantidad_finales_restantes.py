class Indicador_Cantidad_Finales_Restantes():
    def __init__(self, intentos_final):
        self
        self.intentos_final = intentos_final

    def cantidad_finales_restante(self, finales, materia):
        return self.intentos_final.operacion(finales, materia.cant_veces_final_rendible)