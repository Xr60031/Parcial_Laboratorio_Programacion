import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.regularizado import Regularizado

class TestRegularizado(unittest.TestCase):
    def setUp(self):
        self.funcion = Regularizado()

    def test_todas_notas_aprobadas(self):
        notas = [
            Mock(valor_nota=7, valor_recuperatorio=None),
            Mock(valor_nota=8, valor_recuperatorio=None),
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_nota_desaprobada_con_recuperatorio_aprobado(self):
        notas = [
            Mock(valor_nota=5, valor_recuperatorio=7),
            Mock(valor_nota=6, valor_recuperatorio=None),
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_nota_desaprobada_sin_recuperatorio(self):
        notas = [
            Mock(valor_nota=5, valor_recuperatorio=None),
            Mock(valor_nota=7, valor_recuperatorio=None),
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertFalse(resultado)

    def test_nota_desaprobada_con_recuperatorio_desaprobado(self):
        notas = [
            Mock(valor_nota=4, valor_recuperatorio=5),
            Mock(valor_nota=7, valor_recuperatorio=None),
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertFalse(resultado)

    def test_varias_notas_mixed(self):
        notas = [
            Mock(valor_nota=7, valor_recuperatorio=None),
            Mock(valor_nota=3, valor_recuperatorio=6),
            Mock(valor_nota=5, valor_recuperatorio=7),
            Mock(valor_nota=8, valor_recuperatorio=None),
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_lista_vacia(self):
        resultado = self.funcion.operacion([], 6)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
