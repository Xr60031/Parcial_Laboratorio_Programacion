from Dominio.Funciones_sistema.Acciones_sistema.accion import Accion
from Dominio.Materias.materia import Materia

class Agregar(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.ATRIBUTOS = [
            ("id_materia", "ID de la Materia", "int"),
            ("nombre_materia", "Nombre de la Materia", "str"),
            ("nombre_docente", "Nombre de el/la Docente", "str"),
            ("nota_min_aprobar", "Nota mínima para Aprobar un parcial/final", "float"),
            ("es_promocionable", "¿Es promocionable?", "bool"),
            ("nota_min_promocion", "Nota mínima para Promocionar (si aplica)", "float"),
            ("cant_veces_final_rendible", "Cantidad de oportunidades para rendir el final", "int"),
            ("cant_parciales", "Cantidad de parciales de la materia", "int")
        ]
        self.TIPOS = {
            "int": self.entero,
            "float": self.decimal,
            "str": self.cadena,
            "bool": self.booleano
        }
    
    def entero(self):
        return self.main.interfaz_entrada.obtener_entero(self.atributo[1])
    
    def decimal(self):
        return self.main.interfaz_entrada.obtener_decimal(self.atributo[1])
    
    def cadena(self):
        return self.main.interfaz_entrada.obtener_cadena(self.atributo[1])
    
    def booleano(self):
        return self.main.interfaz_entrada.obtener_booleano(self.atributo[1])

    def cambiar_a_mostrar(self):
        from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)

    def hacer_accion(self):
        datos = []

        for i in len(self.ATRIBUTOS):
            dato = self.TIPOS[self.ATRIBUTOS[i][2]]()
            datos.append(dato)
        
        nueva_materia = Materia(tuple(datos))

        self.main.persistencia.agregar_materia(nueva_materia)

        self.main.interfaz_salida.mostrar_advertencia("materia_agregada")

        self.cambiar_a_mostrar()