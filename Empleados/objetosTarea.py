from empleados import *

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

               