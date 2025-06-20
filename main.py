from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Manejo_consola.cli import CLI
from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla

class Main():
    def __init__(self):
        self.persistencia = Facade_Persistencia()
        self.builder_determinador = Builder_Determinador()
        self.interfaz_entrada = CLI()
        self.interfaz_salida = self.interfaz_entrada
        self.accion = Mostrar_Tabla(self)

    def main(self):
        self.persistencia.conectar()
        self.persistencia.crear_base()  

        while True:
            self.accion.hacer_accion()

if __name__ == "__main__":
    main_ = Main()
    main_.main()