from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado

"""
-> Se quiere saber el estado de X materia
-> Calculador(Materia -> Criterio, notas parciales, notas finales)
-> Funciones con criterio para determinar el estado de la materia
-> Minma cant parciales (1 - Para saber si esta cursando -> False = Cursando
-> Desaprobadas con recuperatorio (2 True = Cursando
-> Promociona (3 True = Promocionado
-> Aprobado (4 True = Aprobó
-> Regularizado (5 True = Regularizado
-> Intentos_Final (6 0 = Desaprobado


Funcion para finales
-> Intentos_Final (1
"""

class Determinador_Estado():
    def __init__(self, 
            aprobado = None, 
            desaprobadas_sin_recuperatorio = None, 
            promociona = None,
            intentos_final_restante = None,
            regularizado = None,
            minima_cantidad_parciales = None):
        self.aprobado = aprobado
        self.desaprobadas_sin_recuperatorio = desaprobadas_sin_recuperatorio
        self.promociona = promociona
        self.intentos_final = intentos_final_restante
        self.regularizado = regularizado
        self.minima_cant_parciales = minima_cantidad_parciales

    def esta_cursando(self, notas_parciales, materia):
        return not self.minima_cant_parciales.operacion(notas_parciales, materia.cant_parciales) or self.desaprobadas_sin_recuperatorio.operacion(notas_parciales, materia.nota_min_aprobar)

    def promociono(self, notas_parciales, materia):
        return materia.es_promocionable and self.promociona.operacion(notas_parciales, materia.nota_min_promocion)

    def aprobo(self, notas_finales, materia):
        return self.aprobado.operacion(notas_finales, materia.nota_min_aprobar)
    
    def regularizo(self, notas_parciales, materia):
        return self.regularizado.operacion(notas_parciales, materia.nota_min_aprobar) and self.intentos_final.operacion(notas_parciales, materia.cant_veces_final_rendible) > 0
    
    def consultar_estado(self, notas_parciales, notas_finales, materia):
        if(self.esta_cursando(notas_parciales, materia)):
            return Estado.CURSANDO
        elif(self.promociono(notas_parciales, materia)):
            return Estado.PROMOCIONADO
        elif(self.aprobo(notas_finales, materia)):
            return Estado.APROBADO
        elif(self.regularizo(notas_parciales, materia)):
            return Estado.REGULARIZADO
        else: 
            return Estado.DESAPROBADO



