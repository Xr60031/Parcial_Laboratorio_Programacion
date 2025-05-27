import sqlite3

conn = sqlite3.connect('plantilla.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Usuario (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        email TEXT
    )
''')
conn.commit()
conn.close()
