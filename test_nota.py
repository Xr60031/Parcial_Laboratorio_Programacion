import unittest
from Dominio.Materias.nota import Nota

class TestNota(unittest.TestCase):

    def setUp(self):
        self.datos = (
            101,   # id_nota
            1,     # id_materia
            8.5    # valor_nota
        )
        self.nota = Nota(self.datos)

    def test_constructor(self):
        self.assertEqual(self.nota.id_nota, 101)
        self.assertEqual(self.nota.id_materia, 1)
        self.assertEqual(self.nota.valor_nota, 8.5)

    def test_getters(self):
        self.assertEqual(self.nota.get_id_nota(), 101)
        self.assertEqual(self.nota.get_id_materia(), 1)
        self.assertEqual(self.nota.get_valor_nota(), 8.5)

    def test_setters(self):
        self.nota.set_id_nota(202)
        self.assertEqual(self.nota.get_id_nota(), 202)

        self.nota.set_id_materia(2)
        self.assertEqual(self.nota.get_id_materia(), 2)

        self.nota.set_valor_nota(9.0)
        self.assertEqual(self.nota.get_valor_nota(), 9.0)

if __name__ == '__main__':
    unittest.main()
