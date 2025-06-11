from abc import ABC, abstractmethod

class Accion(ABC):
    def __init__(self, main):
        super().__init__()
        self.main = main

    @abstractmethod
    def hacer_accion(self):
        pass