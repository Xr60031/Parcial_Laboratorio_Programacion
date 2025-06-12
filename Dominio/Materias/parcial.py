from Dominio.Materias.nota import Nota

class Parcial(Nota):
    def __init__(self, tupla):
        super().__init__(tupla)
        self.valor_recuperatorio = tupla[3]

    def get_valor_recuperatorio(self):
        return self.valor_recuperatorio
    
    def set_valor_recuperatorio(self, valor):
        self.valor_recuperatorio = valor