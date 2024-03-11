import sqlite3
from dataclasses import dataclass, astuple


@dataclass
class Empleado:
    id: int
    name: str
    salario: float = 0

conn = sqlite3.connect('pelis.db')
cursor = conn.cursor()

# e = Empleado(8, 'Tina', 1500)
# # print(astuple(e))
# cursor.execute("INSERT INTO empleados (id, nombre, salario) VALUES (?,?, ?);", astuple(e))

# cursor.execute("DELETE FROM empleados WHERE ID = 6")
cursor.execute("SELECT * FROM empleados;")

empleados: list[Empleado]  = cursor.fetchall()

for row in empleados:
  empleado: Empleado = Empleado(*row)  # convert row into an Empleado class, unpack
  print(empleado.id, empleado.name, empleado.salario)  # row is now an object Empleado

conn.commit()
conn.close()