from abc import ABC, abstractmethod

class Interfaz_Input(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_entero(self, entero_a_obtener):
        pass

    @abstractmethod
    def seleccionar_opcion(self, opciones_disponibles):
        pass