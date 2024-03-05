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


class Sistemas_Nominas():
    def __init__(self, empleados) -> None:
       self.empleados = empleados
 
    def calcular_nominas(self):
      print('Calculando nominas')
      print('___________________')
      for empleado in self.empleados:
        print(f'Nomina para: {empleado.nombre} - {empleado.puesto}')
        print(f'- $: {empleado.calcular_nomina():.2f}')
        print('')


# --------Main---------
empleados = []        

jon = Programador('Jon', 1200, 'Programador', 'JAVA')
tom = Programador('Tom', 1000, 'Programador', 'php')
ane = Empleado('Ane', 1300, 'Analista')

empleados.append(jon)
empleados.append(tom)
empleados.append(ane)
nominas = Sistemas_Nominas(empleados)
nominas.calcular_nominas()

               