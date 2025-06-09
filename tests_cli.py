import unittest
from unittest.mock import patch
from Dominio.Funciones_sistema.Manejo_consola.cli import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    @patch('builtins.input', return_value='Juan')
    def test_obtener_dato(self, mock_input):
        dato = self.cli.obtener_dato("nombre")
        mock_input.assert_called_once_with("Ingrese nombre: ")
        self.assertEqual(dato, "Juan")

    @patch('builtins.print')
    def test_mostrar_datos(self, mock_print):
        mensajes = ["Hola", "Mundo"]
        self.cli.mostrar_datos(mensajes)
        mock_print.assert_called_once_with(mensajes, sep="\t")

if __name__ == '__main__':
    unittest.main()
