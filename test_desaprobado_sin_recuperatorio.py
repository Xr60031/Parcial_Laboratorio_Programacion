import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.desaprobadas_sin_recuperatorio import Desaprobadas_Sin_Recuperatorio

class TestDesaprobadasSinRecuperatorio(unittest.TestCase):
    def setUp(self):
        self.funcion = Desaprobadas_Sin_Recuperatorio()

    def test_una_nota_desaprobada_sin_recuperatorio(self):
        nota = Mock(valor_nota=3, valor_recuperatorio=None)
        resultado = self.funcion.operacion([nota], 6)
        self.assertTrue(resultado)

    def test_una_nota_desaprobada_con_recuperatorio(self):
        nota = Mock(valor_nota=3, valor_recuperatorio=7)
        resultado = self.funcion.operacion([nota], 6)
        self.assertFalse(resultado)

    def test_nota_aprobada(self):
        nota = Mock(valor_nota=7, valor_recuperatorio=None)
        resultado = self.funcion.operacion([nota], 6)
        self.assertFalse(resultado)

    def test_varias_notas_una_desaprobada_sin_recuperatorio(self):
        notas = [
            Mock(valor_nota=7, valor_recuperatorio=None),
            Mock(valor_nota=4, valor_recuperatorio=None),
            Mock(valor_nota=5, valor_recuperatorio=7)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_varias_notas_ninguna_cumple_condicion(self):
        notas = [
            Mock(valor_nota=7, valor_recuperatorio=None),
            Mock(valor_nota=5, valor_recuperatorio=7),
            Mock(valor_nota=6, valor_recuperatorio=None)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertFalse(resultado)

    def test_lista_vacia(self):
        resultado = self.funcion.operacion([], 6)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main(verbosity=2)
