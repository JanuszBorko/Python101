class Madre:
    def deportes(self):
        print("Me gusta hacer deportes")

class Padre:
    def cocinar(self):
        print("Me gusta cocinar")

class Hijo(Madre, Padre):
    pass


#---------Main-----

jon = Hijo()
jon.cocinar()
jon.deportes()