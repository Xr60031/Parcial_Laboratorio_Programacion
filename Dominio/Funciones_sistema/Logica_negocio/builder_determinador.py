from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.aprobado import Aprobado
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.desaprobadas_sin_recuperatorio import Desaprobadas_Sin_Recuperatorio
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.promociona import Promociona
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.regularizado import Regularizado
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.minima_cantidad_parciales import Minima_Cantidad_Parciales
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado

class Builder_Determinador():
    def __init__(self):
        self
        self.reset()
    
    def set_aprobado(self):
        self.resultado.aprobado = Aprobado()

    def set_desaprobadas_sin_recuperatorio(self):
        self.resultado.desaprobadas_sin_recuperatorio = Desaprobadas_Sin_Recuperatorio()

    def set_promociona(self):
        self.resultado.promociona = Promociona()

    def set_intentos_final_restante(self):
        self.resultado.intentos_final = Intentos_Final_Restante()

    def set_regularizado(self):
        self.resultado.regularizado = Regularizado()

    def set_minima_cantidad_parciales(self):
        self.resultado.minima_cant_parciales = Minima_Cantidad_Parciales()

    def reset(self):
        self.resultado = Determinador_Estado()

    def construir(self):
        self.set_aprobado()
        self.set_desaprobadas_sin_recuperatorio()
        self.set_promociona()
        self.set_intentos_final_restante()
        self.set_regularizado()
        self.set_minima_cantidad_parciales()
    
    def get_resultado(self):
        return self.resultado