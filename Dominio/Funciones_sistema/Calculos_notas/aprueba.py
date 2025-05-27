from Dominio.Funciones_sistema.Calculos_notas.funcion import Funcion

class Aprueba(Funcion):
    def __init__(self):
        super().__init__()

    def operacion(self, notas, nota_aprobada):
        #Lanzar Excepcion si len(notas)== 0 o si hay una nota > 10 o < 1
        i = 0
        cant_notas = len(notas)
        aprobado = True
        while i < cant_notas -1 and aprobado == True:
            if notas[i] < nota_aprobada:
                if i+1 <= cant_notas:
                    if notas[i+1] < nota_aprobada:
                        aprobado = False
                else:
                    aprobado = False
            
            i = i+2

        return aprobado
