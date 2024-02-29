from time import sleep

class Bebidas:
    def __init__(self, taza:str, tipo:str, volumen:int) -> None:
        self.taza = taza
        self.tipo = tipo
        self.volumen = volumen

    
    def __str__(self) -> str:
        return f"Bebidas.tipo, Bebidas.taza, Bebidas.volumen"

    def resumen(self):
        print(f"Has pedido {self.tipo} en {self.taza} de {self.volumen}ml\n")
    
    def beber(self,c):
        self.volumen = int(self.volumen) - c

# -----------------------------main program
        
print("Bienvenido en CafeBucks")

pedido: bool = True
listaBebidas = []

while pedido == True:

    tipo: str = input("Que quiere tomar? ")
    taza: str = input("Lo quieres en baso o en una taza? ")
    tamano: int = input("Que tamaño quiere: 150ml / 250ml / 500ml? ")
    
    if input("Quiere algo más Y/N?? ").upper() == "N": pedido = False

    bebida = Bebidas(taza, tipo, tamano)
    listaBebidas.append(bebida)

print("\n")

trago = int(input("Cuanto quieres beber"))
cantidad = bebida.beber(trago)
print(cantidad)    



# tipo = "Has pedido " + input("Que quiere beber ahora: ")
# for tipo in listaBebidas:
#     print(tipo)

print("\nGracias por tu pedido \n")


