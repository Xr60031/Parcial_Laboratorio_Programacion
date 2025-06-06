from abc import ABC, abstractmethod

class Interfaz_Output(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def mostrar_datos(self, lista_mensajes):
        pass