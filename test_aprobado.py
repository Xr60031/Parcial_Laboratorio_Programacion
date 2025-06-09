import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.aprobado import Aprobado

class TestAprobado(unittest.TestCase):
    def setUp(self):
        self.aprobado = Aprobado()

    def test_una_nota_aprobada(self):
        nota1 = Mock(valor_nota=8)
        notas = [nota1]
        resultado = self.aprobado.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_nota_exactamente_criterio(self):
        nota1 = Mock(valor_nota=6)
        notas = [nota1]
        resultado = self.aprobado.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_ninguna_nota_aprobada(self):
        notas = [Mock(valor_nota=3), Mock(valor_nota=5)]
        resultado = self.aprobado.operacion(notas, 6)
        self.assertFalse(resultado)

    def test_varias_notas_con_una_aprobada(self):
        notas = [Mock(valor_nota=2), Mock(valor_nota=7), Mock(valor_nota=4)]
        resultado = self.aprobado.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_lista_vacia(self):
        notas = []
        resultado = self.aprobado.operacion(notas, 6)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
