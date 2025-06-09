import unittest
from Dominio.Materias.materia import Materia

class TestMateria(unittest.TestCase):

    def setUp(self):
        self.datos = (
            1,                    # id_materia
            "Matemática",         # nombre_materia
            "Prof. López",        # nombre_docente
            4.0,                  # nota_min_aprobar
            True,                 # es_promocionable
            7.0,                  # nota_min_promocion
            3,                    # cant_veces_final_rendible
            2                     # cant_parciales
        )
        self.materia = Materia(self.datos)

    def test_constructor(self):
        self.assertEqual(self.materia.id_materia, self.datos[0])
        self.assertEqual(self.materia.nombre_materia, self.datos[1])
        self.assertEqual(self.materia.nombre_docente, self.datos[2])
        self.assertEqual(self.materia.nota_min_aprobar, self.datos[3])
        self.assertEqual(self.materia.es_promocionable, self.datos[4])
        self.assertEqual(self.materia.nota_min_promocion, self.datos[5])
        self.assertEqual(self.materia.cant_veces_final_rendible, self.datos[6])
        self.assertEqual(self.materia.cant_parciales, self.datos[7])

    def test_getters(self):
        self.assertEqual(self.materia.get_id_materia(), 1)
        self.assertEqual(self.materia.get_nombre_materia(), "Matemática")
        self.assertEqual(self.materia.get_nombre_docente(), "Prof. López")
        self.assertEqual(self.materia.get_nota_min_aprobar(), 4.0)
        self.assertEqual(self.materia.get_es_promocionable(), True)
        self.assertEqual(self.materia.get_nota_min_promocion(), 7.0)
        self.assertEqual(self.materia.get_cant_veces_rendible_final(), 3)
        self.assertEqual(self.materia.get_cant_parciales(), 2)

    def test_setters(self):
        self.materia.set_id_materia(2)
        self.assertEqual(self.materia.get_id_materia(), 2)

        self.materia.set_nombre_materia("Física")
        self.assertEqual(self.materia.get_nombre_materia(), "Física")

        self.materia.set_nombre_docente("Prof. García")
        self.assertEqual(self.materia.get_nombre_docente(), "Prof. García")

        self.materia.set_nota_min_aprobar(5.0)
        self.assertEqual(self.materia.get_nota_min_aprobar(), 5.0)

        self.materia.set_es_promocionable(False)
        self.assertEqual(self.materia.get_es_promocionable(), False)

        self.materia.set_nota_min_promocion(8.0)
        self.assertEqual(self.materia.get_nota_min_promocion(), 8.0)

        self.materia.set_cant_veces_rendible_final(4)
        self.assertEqual(self.materia.get_cant_veces_rendible_final(), 4)

        self.materia.set_cant_parciales(3)
        self.assertEqual(self.materia.get_cant_parciales(), 3)

if __name__ == '__main__':
    unittest.main()