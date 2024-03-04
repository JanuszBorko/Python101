class Madre:
    def deportes(self):
        print("Me gusta hacer deportes")
    def cocinar(self):
        print("La madre le gusta cocinar")

class Padre:
    def cocinar(self):
        print("El padre le gusta cocinar")

class Hijo(Padre, Madre): #importante el orden MRO (method Resolution )
    pass


#---------Main-----

jon = Hijo()
jon.cocinar()
jon.deportes()