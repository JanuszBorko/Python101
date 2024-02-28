class Guitarra:
    def __init__(self, marca, cuerdas) -> None:   # definimos atributos a traves de constructor
        self.marca = marca
        self.cuerdas = cuerdas

    def tocar(self):
        print(f"soy {self.marca} y brrn, brnnn, brennnn")

# main program - instanciar / usar la clase

nombre = input("Cual es le nombre de la guitarra ")
guit1 = Guitarra(nombre, 6)
print(guit1.marca)
print(guit1.cuerdas)
# bajo = Guitarra("bajo sencillo", 4)
# bajo.cuerdas=5
# print(bajo.cuerdas)
guit1.tocar()

