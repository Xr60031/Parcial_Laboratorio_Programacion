from abc import ABC, abstractmethod

class Accion(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def hacer_accion(self, main):
        pass