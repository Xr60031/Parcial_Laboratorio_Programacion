from Dominio.Funciones_sistema.Calculos_notas.funcion_con_criterio import Funcion_Con_Criterio

class Intentos_Final_Restante(Funcion_Con_Criterio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, criterio):
        return criterio - len(notas)
