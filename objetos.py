class Guitarra:
    def __init__(self, marca, cuerdas = 6) -> None:   # definimos atributos a traves de constructor
        self.marca = marca
        self.cuerdas = cuerdas
        self._precio = 100          # medio privado


    def __str__(self):
        return "hola guitarra"

    def tocar(self):
        print(f"soy {self.marca} y brrn, brnnn, brennnn")
        
    def romperCuerdas(self, cuerdasRotas):
        self.cuerdas = self.cuerdas - cuerdasRotas
        print(f"Me he quedado con {self.cuerdas} cuerdas")



# main program - instanciar / usar la clase

# nombre = input("Cual es le nombre de la guitarra ")
# guit1 = Guitarra(nombre)
# print(guit1.marca)
# print(guit1.cuerdas)
# # bajo = Guitarra("bajo sencillo", 4)
# # bajo.cuerdas=5
# # print(bajo.cuerdas)
# guit1.tocar()
# print(guit1)

guit = Guitarra("Les Paul", 6)
print(guit.cuerdas)
guit.romperCuerdas(1)
print(guit.cuerdas)