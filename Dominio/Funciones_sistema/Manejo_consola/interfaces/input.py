from abc import ABC, abstractmethod

class Interfaz_Input(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_dato(self, nombre_dato_a_obtener):
        pass