print("Programa BD")

import sqlite3

conn = sqlite3.connect('pelis2.db')

#conn.execute("CREATE TABLE Pelis (id integer primary key autoincrement, nombre text, duracion real)")

head = ["id", "nombre", "duracion"]

while True:

    accion = int(input("Que quieres hacer? 1. SHOW ALL, 2. SELECTED, 3. INSERT, 4. UPDATE, 5. DELETE, 6. Stop "))

    match accion:
        case 1: # mostrar todas las pelis
            cur = conn.cursor()
            cur.execute("SELECT * FROM Pelis;")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        case 2:
            buscar = input("Que pelicula quieres buscar (3 primeras letras): ")
            buscar = buscar + "%"
            sSQL = f"SELECT * FROM Pelis WHERE nombre LIKE ?"
            cur = conn.cursor()
            cur.execute(sSQL, (buscar,))  #importante añadir ,
            rows = cur.fetchall()
            for row in rows:
                print(row)

        case 3:
            nombre = input("Que pelicula quieres añadir: ")
            duracion = input("Que duración tiene: ")
            entrada = (nombre, duracion)
            cur=conn.cursor()
            cur.execute("INSERT INTO PELIS (nombre, duracion) VALUES (?, ?);", entrada)
            conn.commit()

        case 4:
            ref = int(input("Que referencia quieres actualiazar: "))
            columna = int(input("Que campo quieres cambiar: 1. Titulo, 2. Duracion ? "))
            sSQL = f"UPDATE Pelis SET {head[columna]}=? WHERE id=?"
            valor = input("Introduce el valor correcto: ")
            cur = conn.cursor()
            cur.execute(sSQL, (valor, ref))

        case 5:
            ref = int(input("Que referencia quieres borrar: "))
            sSQL = f"DELETE FROM Pelis WHERE id={ref}"
            cur = conn.cursor()
            cur.execute(sSQL)

        case 6:
            conn.commit()
            conn.close
            break

