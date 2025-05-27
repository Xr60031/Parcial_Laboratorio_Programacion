from Dominio.Funciones_sistema.Calculos_notas.funcion import Funcion

class Promedio(Funcion):
    def __init__(self):
        super().__init__()

    def operacion(self, notas):
        cant_notas_sin_ceros = len([n for n in notas if n != 0])
        cant_notas = len(notas)
        suma_notas = 0
        for i in range(cant_notas):
            if notas[i] != 0:
                suma_notas += notas[i]

        return suma_notas/cant_notas_sin_ceros
