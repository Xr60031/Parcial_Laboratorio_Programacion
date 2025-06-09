import unittest
from unittest.mock import MagicMock
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado

class DummyMateria:
    def __init__(self, cant_parciales=2, nota_min_aprobar=4, nota_min_promocion=7,
        es_promocionable=True, cant_veces_final_rendible=2):
        self.cant_parciales = cant_parciales
        self.nota_min_aprobar = nota_min_aprobar
        self.nota_min_promocion = nota_min_promocion
        self.es_promocionable = es_promocionable
        self.cant_veces_final_rendible = cant_veces_final_rendible

class TestDeterminadorEstado(unittest.TestCase):
    def setUp(self):
        self.minima_cant_parciales = MagicMock()
        self.desaprobadas_sin_recuperatorio = MagicMock()
        self.promociona = MagicMock()
        self.aprobado = MagicMock()
        self.intentos_final = MagicMock()
        self.regularizado = MagicMock()

        self.det = Determinador_Estado(
            aprobado=self.aprobado,
            desaprobadas_sin_recuperatorio=self.desaprobadas_sin_recuperatorio,
            promociona=self.promociona,
            intentos_final_restante=self.intentos_final,
            regularizado=self.regularizado,
            minima_cantidad_parciales=self.minima_cant_parciales
        )

        self.materia = DummyMateria()
        self.notas_parciales = [5, 6]
        self.notas_finales = [7]

    def test_esta_cursando_por_minima_cant_parciales_false(self):
        self.minima_cant_parciales.operacion.return_value = False
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.assertTrue(self.det.esta_cursando(self.notas_parciales, self.materia))

    def test_esta_cursando_por_desaprobadas_true(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = True
        self.assertTrue(self.det.esta_cursando(self.notas_parciales, self.materia))

    def test_no_esta_cursando(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.assertFalse(self.det.esta_cursando(self.notas_parciales, self.materia))

    def test_promociono_true(self):
        self.promociona.operacion.return_value = True
        self.assertTrue(self.det.promociono(self.notas_parciales, self.materia))

    def test_promociono_false_si_materia_no_es_promocionable(self):
        self.materia.es_promocionable = False
        self.assertFalse(self.det.promociono(self.notas_parciales, self.materia))

    def test_aprobo_true(self):
        self.aprobado.operacion.return_value = True
        self.assertTrue(self.det.aprobo(self.notas_finales, self.materia))

    def test_regularizo_true(self):
        self.regularizado.operacion.return_value = True
        self.intentos_final.operacion.return_value = 1
        self.assertTrue(self.det.regularizo(self.notas_parciales, self.materia))

    def test_regularizo_false_si_intentos_0(self):
        self.regularizado.operacion.return_value = True
        self.intentos_final.operacion.return_value = 0
        self.assertFalse(self.det.regularizo(self.notas_parciales, self.materia))

    def test_regularizo_false_si_no_regulariza(self):
        self.regularizado.operacion.return_value = False
        self.intentos_final.operacion.return_value = 2
        self.assertFalse(self.det.regularizo(self.notas_parciales, self.materia))

    def test_consultar_estado_cursando(self):
        self.minima_cant_parciales.operacion.return_value = False
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        estado = self.det.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.CURSANDO)

    def test_consultar_estado_promocionado(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.promociona.operacion.return_value = True
        estado = self.det.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.PROMOCIONADO)

    def test_consultar_estado_aprobado(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.promociona.operacion.return_value = False
        self.aprobado.operacion.return_value = True
        estado = self.det.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.APROBADO)

    def test_consultar_estado_regularizado(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.promociona.operacion.return_value = False
        self.aprobado.operacion.return_value = False
        self.regularizado.operacion.return_value = True
        self.intentos_final.operacion.return_value = 1
        estado = self.det.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.REGULARIZADO)

    def test_consultar_estado_desaprobado(self):
        self.minima_cant_parciales.operacion.return_value = True
        self.desaprobadas_sin_recuperatorio.operacion.return_value = False
        self.promociona.operacion.return_value = False
        self.aprobado.operacion.return_value = False
        self.regularizado.operacion.return_value = False
        estado = self.det.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.DESAPROBADO)

if __name__ == '__main__':
    unittest.main()
