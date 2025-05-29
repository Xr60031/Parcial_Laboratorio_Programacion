from Dominio.Funciones_sistema.Calculos_notas.funcion_con_criterio import Funcion_Con_Criterio

class Promociona(Funcion_Con_Criterio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, criterio):
        i = 0
        cant_notas = len(notas)
        promociona = True
        while i < cant_notas and promociona == True:
            if notas[i].valor_nota < criterio:
                promociona = False
            i = i+1

        return promociona
