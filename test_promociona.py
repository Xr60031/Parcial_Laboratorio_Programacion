import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.promociona import Promociona

class TestPromociona(unittest.TestCase):
    def setUp(self):
        self.funcion = Promociona()

    def test_todas_las_notas_aprobadas(self):
        notas = [
            Mock(valor_nota=7),
            Mock(valor_nota=8),
            Mock(valor_nota=6)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_una_nota_desaprobada(self):
        notas = [
            Mock(valor_nota=7),
            Mock(valor_nota=5),
            Mock(valor_nota=8)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertFalse(resultado)

    def test_todas_las_notas_justas(self):
        notas = [
            Mock(valor_nota=6),
            Mock(valor_nota=6)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertTrue(resultado)

    def test_lista_vacia(self):
        resultado = self.funcion.operacion([], 6)
        self.assertFalse(resultado)

    def test_todas_malas(self):
        notas = [
            Mock(valor_nota=2),
            Mock(valor_nota=3),
            Mock(valor_nota=4)
        ]
        resultado = self.funcion.operacion(notas, 6)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
