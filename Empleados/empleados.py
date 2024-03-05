class Empleado:
    def __init__(self, nombre, nomina, puesto) -> None:
      self.nombre = nombre
      self.puesto = puesto
      self.nomina = float(nomina)
    def calcular_nomina(self):
       return self.nomina*1.1
       
class Programador(Empleado):
    def __init__(self, nombre, nomina, puesto, lenguaje) -> None:
      super().__init__(nombre, nomina, puesto)
      self.lenguaje = lenguaje

    def calcular_nomina(self):
       if self.lenguaje == "JAVA":
        return self.nomina*1.4
       else:
        return self.nomina*1.2

