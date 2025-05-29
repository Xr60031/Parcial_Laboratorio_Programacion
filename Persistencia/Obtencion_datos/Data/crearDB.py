import sqlite3

class CrearDatabase():
    conn = sqlite3.connect('plantilla.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE Materia (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            docente TEXT,
            nota_min_aprobar INTEGER
            es_promocionable BOOLEAN
            nota_min_promocion INTEGER
            cant_veces_final_rendible INTEGER
        );
        
        CREATE TABLE Parcial (
            id INTEGER PRIMARY KEY,
            materia INTEGER,
            valor INTEGER,
            valor_recuperatorio INTEGER
        );
        
        CREATE TABLE Final (
            id INTEGER PRIMARY KEY,
            materia INTEGER,
            valor INTEGER
        )           
        
    ''')
    conn.commit()
    conn.close()


