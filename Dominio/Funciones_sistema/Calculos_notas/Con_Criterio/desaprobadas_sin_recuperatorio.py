from Dominio.Funciones_sistema.Calculos_notas.funcion_con_criterio import Funcion_Con_Criterio

class Desaprobadas_Sin_Recuperatorio(Funcion_Con_Criterio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, criterio):
        desaprobada_sin_recuperatorio = False
        i = 0
        while(i < len(notas) and desaprobada_sin_recuperatorio == False):
            if(notas[i].valor_nota < criterio and not notas[i].valor_recuperatorio):
                desaprobada_sin_recuperatorio = True
        return desaprobada_sin_recuperatorio