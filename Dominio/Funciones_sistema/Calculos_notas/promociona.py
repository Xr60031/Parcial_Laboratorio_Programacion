from Dominio.Funciones_sistema.Calculos_notas.funcion import Funcion

class Promociona(Funcion):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, nota_promocion):
        #Lanzar Excepcion si len(notas)== 0 o si hay una nota > 10 o < 1
        i = 0
        cant_notas = len(notas)
        promociona = True
        while i < cant_notas -1 and promociona == True:
            if notas[i] < nota_promocion:
                promociona = False
            i = i+2

        return promociona
