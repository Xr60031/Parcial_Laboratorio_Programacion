from abc import ABC, abstractmethod

class Funcion_Sin_Crierio(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def operacion(self, nota):
        pass