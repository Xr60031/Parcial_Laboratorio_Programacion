class Materia():
    def __init__(self, tupla):
        self.id_materia = tupla[0]
        self.nombre_materia = tupla[1]
        self.nombre_docente = tupla[2]
        self.nota_min_aprobar = tupla[3]
        self.es_promocionable = tupla[4]
        self.nota_min_promocion = tupla[5]
        self.cant_veces_final_rendible = tupla[6]
        self.cant_parciales = tupla[7]

    def get_id_materia(self):
        return self.id_materia

    def set_id_materia(self, id):
        self.id_materia = id
    
    def get_nombre_materia(self):
        return self.nombre_materia

    def set_nombre_materia(self, nombre):
        self.nombre_materia = nombre

    def get_nombre_docente(self):
        return self.nombre_docente
    
    def set_nombre_docente(self, nombre):
        self.nombre_docente = nombre

    def get_nota_min_aprobar(self):
        return self.nota_min_aprobar
    
    def set_nota_min_aprobar(self, nota_minima):
        self.nota_min_aprobar = nota_minima

    def get_es_promocionable(self):
        return self.es_promocionable
    
    def set_es_promocionable(self, es_promocionable):
        self.es_promocionable = es_promocionable

    def get_nota_min_promocion(self):
        return self.nota_min_promocion
    
    def set_nota_min_promocion(self, nota_minima):
        self.nota_min_promocion = nota_minima

    def get_cant_veces_rendible_final(self):
        return self.cant_veces_final_rendible
    
    def set_cant_veces_rendible_final(self, cant):
        self.cant_veces_final_rendible = cant

    def get_cant_parciales(self):
        return self.cant_parciales
    
    def set_cant_parciales(self, cantidad):
        self.cant_parciales = cantidad
