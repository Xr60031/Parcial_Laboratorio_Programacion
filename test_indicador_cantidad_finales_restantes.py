import unittest
from unittest.mock import MagicMock, patch
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes

class DummyMateria:
    def __init__(self, cant_veces_final_rendible):
        self.cant_veces_final_rendible = cant_veces_final_rendible

class TestIndicadorCantidadFinalesRestantes(unittest.TestCase):
    @patch('Calculos_notas.Con_Criterio.indicador_cantidad_finales_restantes.Intentos_Final_Restante')
    def test_cantidad_finales_restante(self, MockIntentosFinal):
        # Setup
        mock_operacion = MagicMock(return_value=1)
        MockIntentosFinal.return_value.operacion = mock_operacion

        indicador = Indicador_Cantidad_Finales_Restantes()

        notas_parciales = [3, 5, 4]
        materia = DummyMateria(cant_veces_final_rendible=2)

        # Test
        resultado = indicador.cantidad_finales_restante(notas_parciales, materia)

        # Assert
        mock_operacion.assert_called_once_with(notas_parciales, materia.cant_veces_final_rendible)
        self.assertEqual(resultado, 1)

if __name__ == '__main__':
    unittest.main()
