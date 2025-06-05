import unittest
from unittest.mock import MagicMock
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final

class TestDeterminadorEstado(unittest.TestCase):
    def setUp(self):
        self.determinador = Determinador_Estado()
        self.materia = MagicMock()
        parcial1 = Parcial()
        parcial1.set_valor_nota(6)
        parcial2 = Parcial()
        parcial2.set_valor_nota(7)
        parcial3 = Parcial()
        parcial3.set_valor_nota(5)
        self.notas_parciales = [parcial1, parcial2, parcial3]

        final1 = Final()
        final1.set_valor_nota(4)
        final2 = Final()
        final2.set_valor_nota(5)
        final3 = Final()
        final3.set_valor_nota(9)
        self.notas_finales = [final1]

    def test_esta_cursando_minima_cant_parciales_falsa_y_desaprobadas_true(self):
        self.determinador.minima_cant_parciales.operacion = MagicMock(return_value=False)
        self.determinador.desaprobadas_sin_recuperatorio.operacion = MagicMock(return_value=True)
        result = self.determinador.esta_cursando(self.notas_parciales, self.materia)
        self.assertTrue(result)

    def test_esta_cursando_minima_cant_parciales_true_y_desaprobadas_false(self):
        self.determinador.minima_cant_parciales.operacion = MagicMock(return_value=True)
        self.determinador.desaprobadas_sin_recuperatorio.operacion = MagicMock(return_value=False)
        result = self.determinador.esta_cursando(self.notas_parciales, self.materia)
        self.assertFalse(result)

    def test_promociono_promocionable_y_operacion_true(self):
        self.materia.es_promocionable = True
        self.determinador.promociona.operacion = MagicMock(return_value=True)
        result = self.determinador.promociono(self.notas_parciales, self.materia)
        self.assertTrue(result)

    def test_promociono_no_promocionable(self):
        self.materia.es_promocionable = False
        result = self.determinador.promociono(self.notas_parciales, self.materia)
        self.assertFalse(result)

    def test_aprobo_true(self):
        self.determinador.aprobado.__call__ = MagicMock(return_value=True)
        result = self.determinador.aprobo(self.notas_finales, self.materia)
        self.assertTrue(result)

    def test_aprobo_false(self):
        self.determinador.aprobado.__call__ = MagicMock(return_value=False)
        result = self.determinador.aprobo(self.notas_finales, self.materia)
        self.assertFalse(result)

    def test_regularizo_true(self):
        self.determinador.regularizado.__call__ = MagicMock(return_value=True)
        self.determinador.intentos_final.operacion = MagicMock(return_value=1)
        result = self.determinador.regularizo(self.notas_parciales, self.materia)
        self.assertTrue(result)

    def test_regularizo_false_por_regularizado(self):
        self.determinador.regularizado.__call__ = MagicMock(return_value=False)
        self.determinador.intentos_final.operacion = MagicMock(return_value=1)
        result = self.determinador.regularizo(self.notas_parciales, self.materia)
        self.assertFalse(result)

    def test_regularizo_false_por_intentos(self):
        self.determinador.regularizado.__call__ = MagicMock(return_value=True)
        self.determinador.intentos_final.operacion = MagicMock(return_value=0)
        result = self.determinador.regularizo(self.notas_parciales, self.materia)
        self.assertFalse(result)

    def test_consultar_estado_cursando(self):
        self.determinador.esta_cursando = MagicMock(return_value=True)
        estado = self.determinador.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.CURSANDO)

    def test_consultar_estado_promocionado(self):
        self.determinador.esta_cursando = MagicMock(return_value=False)
        self.determinador.promociono = MagicMock(return_value=True)
        estado = self.determinador.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.PROMOCIONADO)

    def test_consultar_estado_aprobado(self):
        self.determinador.esta_cursando = MagicMock(return_value=False)
        self.determinador.promociono = MagicMock(return_value=False)
        self.determinador.aprobo = MagicMock(return_value=True)
        estado = self.determinador.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.APROBADO)

    def test_consultar_estado_regularizado(self):
        self.determinador.esta_cursando = MagicMock(return_value=False)
        self.determinador.promociono = MagicMock(return_value=False)
        self.determinador.aprobo = MagicMock(return_value=False)
        self.determinador.regularizo = MagicMock(return_value=True)
        estado = self.determinador.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.REGULARIZADO)

    def test_consultar_estado_desaprobado(self):
        self.determinador.esta_cursando = MagicMock(return_value=False)
        self.determinador.promociono = MagicMock(return_value=False)
        self.determinador.aprobo = MagicMock(return_value=False)
        self.determinador.regularizo = MagicMock(return_value=False)
        estado = self.determinador.consultar_estado(self.notas_parciales, self.notas_finales, self.materia)
        self.assertEqual(estado, Estado.DESAPROBADO)

if __name__ == "__main__":
    unittest.main()