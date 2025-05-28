import unittest
from Dominio.Materias.materia import Materia

class Test_Materia(unittest.TestCase):
    
    def test_get_set_nombre_materia(self):
        materia = Materia()
        materia.set_nombre_materia("Matemática")
        self.assertEqual(materia.get_nombre_materia(), "Matemática")

    def test_get_set_nombre_docente(self):
        materia = Materia()
        materia.set_nombre_docente("Prof. García")
        self.assertEqual(materia.get_nombre_docente(), "Prof. García")

    def test_get_set_notas(self):
        materia = Materia()
        notas = [7, 8, 6, 9, 10]
        materia.set_notas(notas)
        self.assertEqual(materia.get_notas(), notas)

    def test_get_set_nota_min_aprobar(self):
        materia = Materia()
        materia.set_nota_min_aprobar(6)
        self.assertEqual(materia.get_nota_min_aprobar(), 6)

    def test_get_set_es_promocionable(self):
        materia = Materia()
        materia.set_es_promocionable(True)
        self.assertTrue(materia.get_es_promocionable())

    def test_get_set_nota_min_promocion(self):
        materia = Materia()
        materia.set_nota_min_promocion(8)
        self.assertEqual(materia.get_nota_min_promocion(), 8)

    def test_get_set_cant_veces_rendible_final(self):
        materia = Materia()
        materia.set_cant_veces_rendible_final(3)
        self.assertEqual(materia.get_cant_veces_rendible_final(), 3)

if __name__ == "__main__":
    unittest.main()