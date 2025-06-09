from Dominio.Funciones_sistema.Calculos_notas.funcion_con_criterio import Funcion_Con_Criterio

class Regularizado(Funcion_Con_Criterio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, criterio):
        i = 0
        cant_notas = len(notas)
        cursado = True
        while i < cant_notas and cursado == True:
            if notas[i].valor_nota < criterio:
                if not notas[i].valor_recuperatorio or notas[i].valor_recuperatorio < criterio:
                    cursado = False
            i += 1
        return cursado and cant_notas > 0
