import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar

class TestMostrar(unittest.TestCase):
    def test_hacer_accion(self):
        mostrar = Mostrar()

        main = Mock()

        materia = Mock()
        materia.get_id_materia.return_value = "MAT123"
        materia.get_nombre_materia.return_value = "Matemáticas"

        main.persistencia.obtener_materias.return_value = [materia]
        main.persistencia.obtener_parciales.return_value = ["parcial1"]
        main.persistencia.obtener_finales.return_value = ["final1"]

        determinador = Mock()
        determinador.consultar_estado.return_value.name = "Aprobado"
        main.builder_determinador.get_resultado.return_value = determinador

        mostrar.hacer_accion(main)

        main.persistencia.obtener_materias.assert_called_once()
        main.persistencia.obtener_parciales.assert_called_once_with(materia)
        main.persistencia.obtener_finales.assert_called_once_with(materia)

        main.builder_determinador.construir.assert_called_once()
        main.builder_determinador.get_resultado.assert_called_once()
        main.builder_determinador.reset.assert_called_once()

        determinador.consultar_estado.assert_called_once_with(
            ["parcial1"], ["final1"], materia
        )

        main.cli.mostrar_datos.assert_called_once_with([
            "MAT123", "Matemáticas", "Aprobado"
        ])
        main.cli.obtener_dato.assert_called_once_with(
            "Accion (Agregar, Eliminar, Mas informacion): "
        )

if __name__ == '__main__':
    unittest.main()
