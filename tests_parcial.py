import unittest
from Dominio.Materias.parcial import Parcial

class TestParcial(unittest.TestCase):

    def setUp(self):
        self.datos = (
            201,   # id_nota
            10,    # id_materia
            6.0    # valor_nota
        )
        self.parcial = Parcial(self.datos)

    def test_constructor(self):
        self.assertEqual(self.parcial.get_id_nota(), 201)
        self.assertEqual(self.parcial.get_id_materia(), 10)
        self.assertEqual(self.parcial.get_valor_nota(), 6.0)
        self.assertIsNone(self.parcial.get_valor_recuperatorio())

    def test_set_get_valor_recuperatorio(self):
        self.parcial.set_valor_recuperatorio(7.5)
        self.assertEqual(self.parcial.get_valor_recuperatorio(), 7.5)

    def test_inherited_setters(self):
        self.parcial.set_id_nota(202)
        self.assertEqual(self.parcial.get_id_nota(), 202)

        self.parcial.set_id_materia(11)
        self.assertEqual(self.parcial.get_id_materia(), 11)

        self.parcial.set_valor_nota(8.0)
        self.assertEqual(self.parcial.get_valor_nota(), 8.0)

if __name__ == '__main__':
    unittest.main()
