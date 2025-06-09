import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.minima_cantidad_parciales import Minima_Cantidad_Parciales

class TestMinimaCantidadParciales(unittest.TestCase):
    def setUp(self):
        self.funcion = Minima_Cantidad_Parciales()

    def test_sin_notas(self):
        resultado = self.funcion.operacion([], 2)
        self.assertTrue(resultado)

    def test_menos_notas_que_criterio(self):
        notas = [Mock()]
        resultado = self.funcion.operacion(notas, 3)
        self.assertTrue(resultado)

    def test_igual_cantidad_que_criterio(self):
        notas = [Mock(), Mock()]
        resultado = self.funcion.operacion(notas, 2)
        self.assertFalse(resultado)

    def test_mas_notas_que_criterio(self):
        notas = [Mock(), Mock(), Mock()]
        resultado = self.funcion.operacion(notas, 2)
        self.assertFalse(resultado)

    def test_criterio_cero(self):
        notas = [Mock()]
        resultado = self.funcion.operacion(notas, 0)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
