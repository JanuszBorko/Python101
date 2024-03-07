import sqlite3

COL_ID = 0
COL_NOMBRE = 1
COL_DURACION = 2

conn = sqlite3.connect('pelis.db')
cur = conn.cursor() 

cur.execute("SELECT * FROM Peliculas;")
rows = cur.fetchall()

#print(type(rows))

for row in rows:
    if "Indiana Jones" in row:
        print(row[COL_DURACION])


conn.close()