class Guitarra:
    def __init__(self, marca, cuerdas = 6) -> None:   # definimos atributos a traves de constructor
        self.marca = marca
        self.cuerdas = cuerdas
        self._precio = 100          # medio privado

    def __str__(self):
        return "hola guitarra"

    def tocar(self):
        if self.cuerdas > 0:
            print(f"soy {self.marca} y brrn, brnnn, brennnn")
        else:
            print(f"No puedes tocar sin cuerdas ")
        
    def romperCuerdas(self, cuerdasRotas):
        if cuerdasRotas <= self.cuerdas:
            self.cuerdas = self.cuerdas - cuerdasRotas
            print(f"Me he quedado con {self.cuerdas} cuerdas")
        else:
            print("No puedes romper más cuerdas de las que tengas")

class GuitarraElectrica(Guitarra):
    def __init__(self, marca, cuerdas, distorsion) -> None: 
        super().__init__(marca, cuerdas)        # para ejecutar el constructor de arriba
        self.distorsion = distorsion

    def tocar(self):
        print(f"soy {self.marca} y brrn, brnnn, brennnn".upper())
# main program - instanciar / usar la clase


guit = GuitarraElectrica("Les Paul", 6,100)
print(guit.cuerdas)
print(guit.distorsion)
guit.tocar()

# while guit.cuerdas > 0:
#     curRotas = int(input("cuantas cuerdas has roto? "))
#     guit.romperCuerdas(curRotas)
#     print(guit.cuerdas)
#     guit.tocar()