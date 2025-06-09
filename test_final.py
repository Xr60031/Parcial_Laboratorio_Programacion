import unittest
from Dominio.Materias.final import Final

class TestFinal(unittest.TestCase):

    def setUp(self):
        self.datos = (
            301,   # id_nota
            20,    # id_materia
            9.0    # valor_nota
        )
        self.final = Final(self.datos)

    def test_inheritance_and_constructor(self):
        self.assertEqual(self.final.get_id_nota(), 301)
        self.assertEqual(self.final.get_id_materia(), 20)
        self.assertEqual(self.final.get_valor_nota(), 9.0)

if __name__ == '__main__':
    unittest.main()
