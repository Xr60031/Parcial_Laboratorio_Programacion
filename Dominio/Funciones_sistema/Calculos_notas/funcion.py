from abc import ABC, abstractmethod

class Funcion(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def operacion(self, nota, criterio_adicional = 0):
        pass