import unittest
import sqlite3
from unittest.mock import MagicMock
from Persistencia.Facade_Persistencia import Facade_Persistencia

class TestFacadePersistencia(unittest.TestCase):
    def setUp(self):
        self.facade = Facade_Persistencia()
        self.facade.conn = sqlite3.connect(":memory:")
        self.facade.cursor = self.facade.conn.cursor()
        self.facade.crear_base()

        # Mock de materia
        self.mock_materia = MagicMock()
        self.mock_materia.get_id_materia.return_value = 1
        self.mock_materia.get_nombre_materia.return_value = "Matemática"
        self.mock_materia.get_nombre_docente.return_value = "Prof. López"
        self.mock_materia.get_nota_min_aprobar.return_value = 6
        self.mock_materia.get_es_promocionable.return_value = True
        self.mock_materia.get_nota_min_promocion.return_value = 8
        self.mock_materia.get_cant_veces_final_rendible.return_value = 3
        self.mock_materia.get_cant_parciales.return_value = 2

        # Mock de parcial
        self.mock_parcial = MagicMock()
        self.mock_parcial.get_id_nota.return_value = None
        self.mock_parcial.get_id_materia.return_value = 1
        self.mock_parcial.get_valor_nota.return_value = 7

        # Mock de final
        self.mock_final = MagicMock()
        self.mock_final.get_id_nota.return_value = None
        self.mock_final.get_id_materia.return_value = 1
        self.mock_final.get_valor_nota.return_value = 8

    def tearDown(self):
        self.facade.conn.close()

    def test_agregar_y_obtener_materia(self):
        self.facade.agregar_materia(self.mock_materia)
        materias = self.facade.obtener_materias()
        self.assertEqual(len(materias), 1)

    def test_eliminar_materia(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.eliminar_materia(1)
        materias = self.facade.obtener_materias()
        self.assertEqual(materias, [])

    def test_modificar_materia(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.modificar_materia(1, "nombre_materia", "Física")
        self.facade.cursor.execute("SELECT nombre_materia FROM Materia WHERE id_materia = 1")
        nombre = self.facade.cursor.fetchone()[0]
        self.assertEqual(nombre, "Física")

    def test_agregar_y_obtener_parcial(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.agregar_parcial(self.mock_parcial)
        parciales = self.facade.obtener_parciales(self.mock_materia)
        self.assertEqual(len(parciales), 1)

    def test_modificar_parcial(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.agregar_parcial(self.mock_parcial)
        self.facade.modificar_parcial(1, "valor_nota", 9)
        self.facade.cursor.execute("SELECT valor_nota FROM Parcial WHERE id_nota = 1")
        valor = self.facade.cursor.fetchone()[0]
        self.assertEqual(valor, 9)

    def test_agregar_y_eliminar_final(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.agregar_final(self.mock_final)
        finales = self.facade.obtener_finales(self.mock_materia)
        self.assertEqual(len(finales), 1)

        self.facade.eliminar_finales(1)
        finales = self.facade.obtener_finales(self.mock_materia)
        self.assertEqual(len(finales), 0)

    def test_recuperatorio(self):
        self.facade.agregar_materia(self.mock_materia)
        self.facade.agregar_parcial(self.mock_parcial)
        self.facade.agregar_recuperatorio(1, 10)
        self.facade.cursor.execute("SELECT valor_recuperatorio FROM Parcial WHERE id_nota = 1")
        self.assertEqual(self.facade.cursor.fetchone()[0], 10)

        self.facade.eliminar_recuperatorio(1)
        self.facade.cursor.execute("SELECT valor_recuperatorio FROM Parcial WHERE id_nota = 1")
        self.assertIsNone(self.facade.cursor.fetchone()[0])

if __name__ == '__main__':
    unittest.main()
