from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Dominio.Funciones_sistema.Manejo_consola.cli import CLI
from Dominio.Funciones_sistema.Acciones_sistema.accion_mostrar import Mostrar

class Main():
    def __init__(self):
        self
        self.persistencia = Facade_Persistencia()
        self.builder_determinador = Builder_Determinador()
        self.cli = CLI()
        self.accion = Mostrar(self)

    def main(self):

        self.persistencia.conectar()
        self.persistencia.crear_base()  

        while(True):
            self.accion.hacer_accion()

if __name__ == "__main__":
    main_ = Main()
    main_.main()