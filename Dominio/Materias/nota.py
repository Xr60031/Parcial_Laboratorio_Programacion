class Nota():
    def __init__(self, tupla):
        self.id_nota = int(tupla[0])
        self.id_materia = int(tupla[1])
        self.valor_nota = int(tupla[2])

    def get_id_nota(self):
        return self.id_nota

    def set_id_nota(self, id):
        self.id_nota = id
    
    def get_id_materia(self):
        return self.id_materia

    def set_id_materia(self, id):
        self.id_materia = id

    def get_valor_nota(self):
        return self.valor_nota

    def set_valor_nota(self, valor):
        self.valor_nota = valor