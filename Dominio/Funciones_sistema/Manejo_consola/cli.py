from Dominio.Funciones_sistema.Manejo_consola.interfaces.input import Interfaz_Input
from Dominio.Funciones_sistema.Manejo_consola.interfaces.output import Interfaz_Output

class CLI(Interfaz_Input, Interfaz_Output):
    def __init__(self):
        super().__init__()

    def obtener_dato(self, nombre_dato_a_obtener):
        return input(f'Ingrese {nombre_dato_a_obtener}: ')
    
    def mostrar_datos(self, lista_mensajes):
        print(lista_mensajes, sep="\t")