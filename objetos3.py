class Madre:
    def deportes(self):
        print("Me gusta hacer deportes")
    def cocinar(self):
        print("La madre le gusta cocinar")

class Padre:
    def cocinar(self):
        print("Me gusta cocinar")

class Hijo(Madre, Padre): #importante el orden MRO (method Resolution )
    pass


#---------Main-----

jon = Hijo()
jon.cocinar()
jon.deportes()