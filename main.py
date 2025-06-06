from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Dominio.Funciones_sistema.Manejo_consola.cli import CLI
"""
def obtener_estado(valor):
    return(
        0 : CURSANDO 
        1 : REGULARIZADO = 1
        2 : APROBADO = 2
        3 : DESAPROBADO = 3
        4 : PROMOCIONADO = 4
    )
"""
def main():
    persistencia = Facade_Persistencia()
    builder_determinador = Builder_Determinador()
    cli = CLI()

    persistencia.conectar()
    persistencia.crear_base()  

    accion = "Mostrar"
    
    while(accion != "Salir"):
        materias = persistencia.obtener_materias()
        for materia in materias:
            parciales = persistencia.obtener_parciales(materia)
            finales = persistencia.obtener_finales(materia)

            builder_determinador.construir()
            determinador = builder_determinador.get_resultado()
            builder_determinador.reset()

            estado_materia = determinador.consultar_estado(parciales, finales, materia)

            cli.mostrar_datos([
                materia.get_id_materia(),
                materia.get_nombre_materia(),
                estado_materia.name
            ]
            )
        accion = cli.obtener_dato("Accion")


if __name__ == "__main__":
    main()