import sqlite3

conn = sqlite3.connect('users2.db')

conn.execute("CREATE TABLE Users (id integer primary key autoincrement, nombre text, salario real)")

sData = [( "Jon", 3000.12),
        ("Jones", 2130.15)]

cur = conn.cursor()   #cursos de editor de base de datos, indica donde incluir lo
# nombre = input("Que pelicula quieres añadir: ")
# duracion = int(input("Que duración tiene: "))
# data = (4, nombre, duracion)

#cur.executemany("INSERT INTO Peliculas (id, nombre, duracion) VALUES (?, ?, ?);", sData)
cur.executemany("INSERT INTO Users (id, nombre, salario) VALUES (?, ?);",sData)
conn.commit()  #default not auto commit!!

conn.close()