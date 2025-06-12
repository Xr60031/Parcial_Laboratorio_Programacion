from abc import ABC, abstractmethod

class Interfaz_Output(ABC):
    def __init__(self):
        super().__init__()
        self.ADVERTENCIAS = {
            "id_inexistente": "Esa ID no está disponible. Intente de nuevo.",
            "no_entero": "No se ingresó un número. Intente de nuevo.",
            "opcion_invalida": "No se ingresó una acción disponible. Intente de nuevo."
        }

    @abstractmethod
    def mostrar_advertencia(self, id_advertencia):
        pass

    @abstractmethod
    def mostrar_tabla(self, materias, persistencia, builder_determinador):
        pass

    @abstractmethod
    def mostrar_info_materia(self, materia_seleccionada, persistencia, builder_determinador):
        pass