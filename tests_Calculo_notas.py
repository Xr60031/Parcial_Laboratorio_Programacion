import unittest
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.cursado import Aprueba
from Dominio.Funciones_sistema.Calculos_notas.Sin_Criterio.promedio import Promedio
from Dominio.Funciones_sistema.Calculos_notas.Con_Criterio.promociona import Promociona
from Dominio.Funciones_sistema.Calculos_notas.funcion_sin_criterio import Funcion

class Test_Materia(unittest.TestCase):
    def test_funcion_aprobar_caso_verdadero(self):
        funcion_aprueba = Aprueba()
        self.assertEqual(
            funcion_aprueba.operacion([8,0,8,0,0], 6),
            True,
            "Error: Ingrese notas validas"
        )

    def test_funcion_aprobar_caso_falso(self):
        funcion_aprueba = Aprueba()
        self.assertEqual(
            funcion_aprueba.operacion([5,5,10,0,0], 6),
            False,
            "Error: Ingrese notas validas"
        )

    def test_funcion_promociona_caso_verdadero(self):
        funcion_promociona = Promociona()
        self.assertEqual(
            funcion_promociona.operacion([8,0,8,0,0], 8),
            True,
            "Error: Ingrese notas validas"
        )

    def test_funcion_promociona_caso_falso(self):
        funcion_promociona = Promociona()
        self.assertEqual(
            funcion_promociona.operacion([5,8,8,0,0], 8),
            False,
            "Error: Ingrese notas validas"
        )

    def test_funcion_promedio(self):
        funcion_promedio = Promedio()
        self.assertEqual(
            funcion_promedio.operacion([8,0,8,0,0]),
            8,
            "Error: Ingrese notas validas"
        )

if __name__ == "__main__":
    unittest.main()