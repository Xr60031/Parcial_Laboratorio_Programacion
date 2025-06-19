from flask import Flask
from Controller.MateriaController import MateriaController
from Controller.Routes import crear_rutas
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Handlers.final_handler import FinalHandler
from Handlers.parcial_handler import ParcialHandler
from Handlers.recuperatorio_handler import RecuperatorioHandler
from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado

facade = Facade_Persistencia()
facade.conectar()
facade.crear_base()

builder = Builder_Determinador()
builder.construir()
determiner = builder.get_resultado()
handlers = {
    "parcial": ParcialHandler(),
    "recuperatorio": RecuperatorioHandler(),
    "final": FinalHandler()
}

controller = MateriaController(facade, determiner, handlers)

app = Flask(__name__)
app.register_blueprint(crear_rutas(controller))

if __name__ == "__main__":
    app.run(debug=True)
