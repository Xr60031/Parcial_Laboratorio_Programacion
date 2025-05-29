from Dominio.Funciones_sistema.Calculos_notas.funcion_con_criterio import Funcion_Con_Criterio

class Aprobado(Funcion_Con_Criterio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, criterio):
        i = 0
        cant_notas = len(notas)
        cursado = False
        while i < cant_notas and cursado == False:
            if notas[i].valor_nota >= criterio:
                    cursado = True
            i = i+1
        return cursado
