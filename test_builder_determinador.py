import unittest
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.aprobado import Aprobado
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.desaprobadas_sin_recuperatorio import Desaprobadas_Sin_Recuperatorio
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.promociona import Promociona
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.regularizado import Regularizado
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.minima_cantidad_parciales import Minima_Cantidad_Parciales
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado

class TestBuilderDeterminador(unittest.TestCase):
    def setUp(self):
        self.builder = Builder_Determinador()

    def test_reset(self):
        self.builder.reset()
        resultado = self.builder.get_resultado()
        self.assertIsInstance(resultado, Determinador_Estado)
        self.assertIsNone(resultado.aprobado)
        self.assertIsNone(resultado.desaprobadas_sin_recuperatorio)
        self.assertIsNone(resultado.promociona)
        self.assertIsNone(resultado.intentos_final)
        self.assertIsNone(resultado.regularizado)
        self.assertIsNone(resultado.minima_cant_parciales)

    def test_set_aprobado(self):
        self.builder.set_aprobado()
        self.assertIsInstance(self.builder.resultado.aprobado, Aprobado)

    def test_set_desaprobadas_sin_recuperatorio(self):
        self.builder.set_desaprobadas_sin_recuperatorio()
        self.assertIsInstance(self.builder.resultado.desaprobadas_sin_recuperatorio, Desaprobadas_Sin_Recuperatorio)

    def test_set_promociona(self):
        self.builder.set_promociona()
        self.assertIsInstance(self.builder.resultado.promociona, Promociona)

    def test_set_intentos_final_restante(self):
        self.builder.set_intentos_final_restante()
        self.assertIsInstance(self.builder.resultado.intentos_final, Intentos_Final_Restante)

    def test_set_regularizado(self):
        self.builder.set_regularizado()
        self.assertIsInstance(self.builder.resultado.regularizado, Regularizado)

    def test_set_minima_cantidad_parciales(self):
        self.builder.set_minima_cantidad_parciales()
        self.assertIsInstance(self.builder.resultado.minima_cant_parciales, Minima_Cantidad_Parciales)

    def test_construir(self):
        self.builder.construir()
        resultado = self.builder.get_resultado()
        self.assertIsInstance(resultado.aprobado, Aprobado)
        self.assertIsInstance(resultado.desaprobadas_sin_recuperatorio, Desaprobadas_Sin_Recuperatorio)
        self.assertIsInstance(resultado.promociona, Promociona)
        self.assertIsInstance(resultado.intentos_final, Intentos_Final_Restante)
        self.assertIsInstance(resultado.regularizado, Regularizado)
        self.assertIsInstance(resultado.minima_cant_parciales, Minima_Cantidad_Parciales)

if __name__ == '__main__':
    unittest.main()
