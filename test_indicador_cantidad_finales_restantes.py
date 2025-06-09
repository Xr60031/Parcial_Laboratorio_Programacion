import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.intentos_final import Intentos_Final_Restante

class DummyMateria:
    def __init__(self, cant_veces_final_rendible):
        self.cant_veces_final_rendible = cant_veces_final_rendible

class TestIndicadorCantidadFinalesRestantes(unittest.TestCase):
    def test_cantidad_finales_restante(self):
        indicador = Indicador_Cantidad_Finales_Restantes(Intentos_Final_Restante())

        finales = [Mock(valor_nota=3), Mock(valor_nota=5), Mock(valor_nota=4)]
        materia = Mock(cant_veces_final_rendible=2)

        resultado = indicador.cantidad_finales_restante(finales, materia)

        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()
