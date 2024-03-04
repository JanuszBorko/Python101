class Direccion:
  def __init__(self, calle, ciudad):
      self.calle = calle
      self.ciudad = ciudad

  def mostrar(self):
      print(self.calle)
      print(self.ciudad)

class Persona:
  def __init__(self, nombre, email):
      self.nombre = nombre
      self.email= email

  def mostrar(self):
      print(self.nombre + ' ' + self.email)

class Contacto(Direccion, Persona):
   def __init__(self, calle, ciudad, nombre, email, activo):
      Direccion.__init__(self, calle, ciudad)
      Persona.__init__(self, nombre, email)
      self.activo = activo

   def mostrar(self):
        Direccion.mostrar(self)
        Persona.mostrar(self)
        #print(f"{self.nombre} tiene un mail {self.email}. Su direccion es {self.calle}, {self.ciudad}")

#  ----Main---
   
jon = Contacto("Calle1", "Ciudad", "Jon", "rere@ss.pl", True)   
print(jon.mostrar())