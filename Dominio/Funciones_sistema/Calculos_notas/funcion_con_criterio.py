from abc import ABC, abstractmethod

class Funcion_Con_Criterio(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def operacion(self, nota, criterio):
        pass