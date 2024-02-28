from time import sleep

class bebidas:
    def __init__(self, taza, tipo, volumen) -> None:
        self.tipo = tipo
        self.taza = taza
        self.volumen = volumen
    
    def beber(self):
        print(f"Estas bebiendo {self.tipo} en {self.taza} de {self.volumen}\n")

# main program
        
print("Bienvenido en CafeBucks")
tipo = input("Que quiere tomar? ")
taza = input("Lo quieres en baso o en una taza? ")
tamano = input("Que tamaño quiere: 150ml / 250ml / 500ml? ")   
bebida = bebidas(taza, tipo, tamano)
print("Gracias por tu pedido \n")

sleep(1)
bebida.beber()
sleep(1)
