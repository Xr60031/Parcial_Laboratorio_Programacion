import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Sin_Criterio.promedio import Promedio

class TestPromedio(unittest.TestCase):
    def setUp(self):
        self.funcion = Promedio()

    def test_varias_notas(self):
        notas = [
            Mock(valor_nota=7),
            Mock(valor_nota=8),
            Mock(valor_nota=6)
        ]
        resultado = self.funcion.operacion(notas)
        self.assertAlmostEqual(resultado, 7.0)

    def test_una_nota(self):
        notas = [Mock(valor_nota=5)]
        resultado = self.funcion.operacion(notas)
        self.assertEqual(resultado, 5)

    def test_lista_vacia(self):
        resultado = self.funcion.operacion([])
        self.assertEqual(resultado, 0)

    def test_notas_con_cero(self):
        notas = [
            Mock(valor_nota=0),
            Mock(valor_nota=10),
        ]
        resultado = self.funcion.operacion(notas)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()
