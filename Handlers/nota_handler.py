from abc import ABC, abstractmethod

class NotaHandler(ABC):
    @abstractmethod
    def agregar(self, materia, nota): pass

