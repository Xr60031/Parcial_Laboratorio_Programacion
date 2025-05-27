from abc import ABC, abstractmethod

class Funcion(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def operacion(self, materia, linea_a_utilizar):
        pass

