import sqlite3

class CrearDatabase():
    conn = sqlite3.connect('plantilla.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE Materia (
            id_materia INTEGER PRIMARY KEY,
            nombre_materia TEXT,
            nombre_docente TEXT,
            nota_min_aprobar INTEGER,
            es_promocionable BOOLEAN,
            nota_min_promocion INTEGER,
            cant_veces_final_rendible INTEGER,
            cant_parciales INTEGER
        );
        
        CREATE TABLE Parcial (
            id_nota INTEGER PRIMARY KEY,
            id_materia INTEGER,
            valor_nota INTEGER,
            valor_recuperatorio INTEGER
        );
        
        CREATE TABLE Final (
            id_nota INTEGER PRIMARY KEY,
            id_materia INTEGER,
            valor_nota INTEGER
        )           
        
    ''')
    conn.commit()
    conn.close()


