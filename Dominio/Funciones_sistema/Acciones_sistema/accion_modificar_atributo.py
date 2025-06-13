from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion

class Modificar_Atributo(Accion):
    def __init__(self, main, materia, atributo):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.atributo = atributo
        self.TIPOS = {
            "int": self.entero,
            "float": self.decimal,
            "str": self.cadena,
            "bool": self.booleano
        }

    def cambiar_a_seleccionar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def entero(self):
        return self.main.interfaz_entrada.obtener_entero(self.atributo[1])
    
    def decimal(self):
        return self.main.interfaz_entrada.obtener_decimal(self.atributo[1])
    
    def cadena(self):
        return self.main.interfaz_entrada.obtener_cadena(self.atributo[1])
    
    def booleano(self):
        return self.main.interfaz_entrada.obtener_booleano(self.atributo[1])

    def modificar_atributo(self):
        valor = self.TIPOS[self.atributo[2]]()
        self.main.persistencia.modificar_materia(self.materia_seleccionada.id_materia, self.atributo, valor)

    def hacer_accion(self):
        self.modificar_atributo()
        self.cambiar_a_seleccionar()