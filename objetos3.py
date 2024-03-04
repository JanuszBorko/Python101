class Madre:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def deportes(self):
        print("Me gusta hacer deportes")
    def cocinar(self):
        print("La madre le gusta cocinar")

class Padre:
    def __init__(self, ojos):
        self.ojos = ojos
    def cocinar(self):
        print("El padre le gusta cocinar")

class Hijo(Madre, Padre): #importante el orden MRO (method Resolution )
    def __init__(self, nombre, edad, ojos, estudios):
        Madre.__init__(self, nombre, edad)  # en vez "super", si queremos definir a que referimos. hay que añadir tambien self
        self.estudios = estudios
        Padre.__init__(self, ojos)

#---------Main-----

jon = Hijo("Jon", 30, "azules", "programacion")
jon.cocinar()
print(jon.nombre)
print(jon.edad)
