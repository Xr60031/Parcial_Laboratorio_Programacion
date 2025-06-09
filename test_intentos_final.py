import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante

class TestIntentosFinalRestante(unittest.TestCase):
    def setUp(self):
        self.funcion = Intentos_Final_Restante()

    def test_sin_notas(self):
        resultado = self.funcion.operacion([], 3)
        self.assertEqual(resultado, 3)

    def test_con_una_nota(self):
        nota = Mock()
        resultado = self.funcion.operacion([nota], 3)
        self.assertEqual(resultado, 2)

    def test_con_dos_notas(self):
        notas = [Mock(), Mock()]
        resultado = self.funcion.operacion(notas, 3)
        self.assertEqual(resultado, 1)

    def test_con_mas_notas_que_criterio(self):
        notas = [Mock(), Mock(), Mock(), Mock()]
        resultado = self.funcion.operacion(notas, 3)
        self.assertEqual(resultado, -1)

    def test_con_notas_igual_que_criterio(self):
        notas = [Mock(), Mock(), Mock()]
        resultado = self.funcion.operacion(notas, 3)
        self.assertEqual(resultado, 0)

    def test_con_criterio_cero(self):
        notas = [Mock()]
        resultado = self.funcion.operacion(notas, 0)
        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()
