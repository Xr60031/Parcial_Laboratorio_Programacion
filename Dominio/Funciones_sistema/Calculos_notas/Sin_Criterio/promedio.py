from Dominio.Funciones_sistema.Calculos_notas.funcion_sin_criterio import Funcion_Sin_Crierio

class Promedio(Funcion_Sin_Crierio):
    def __init__(self):
        super().__init__()

    def operacion(self, notas):
        cant_notas = len(notas)
        if cant_notas == 0:
            return 0
        suma_notas = 0
        for i in range(cant_notas):
            suma_notas += notas[i].valor_nota
        return suma_notas/cant_notas
