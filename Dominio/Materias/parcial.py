from Dominio.Materias.nota import Nota

class Parcial(Nota):
    def __init__(self):
        super().__init__()
        self.valor_recuperatorio = 0

    def get_valor_recuperatorio(self):
        return self.valor_recuperatorio
    
    def set_valor_recuperatorio(self, valor):
        self.valor_recuperatorio = valor