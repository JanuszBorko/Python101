
# lenguaje = input("Cual es tu lenguaje favorito: ")

# # match lenguaje:
# #     case "Python":
# #         print("a mi me gusta python")
# #     case "Java" | "Javascript":
# #         print("Java complicado")
# #     # case "Java Script":
# #     #     print("otro idioma más")
# #     case _:
# #         print("otros caso")


# print(f"{lenguaje:>20}")

# print("""
#       Tienes 3 opciones
#       1 = encender
#       2 = correr
#       3 = parar""")

# comando = int(input("Que quieres hacer: "))

# match comando:
#     case 1:
#         print("estoy encendido")
#     case 2:
#         print("estoy corriendo")        
#     case 3:
#         print("paro")
#     case _:
#         print("no te entiendo")

# def mensaje(sNombre, sAppellido, iEdad):
#     print(f"hola {sNombre} {sAppellido} tu edad es: {iEdad}")
#     print("adios")


# def sumar(x, y):
#     return x + y
    
# def restar(x, y):
#     return x - y
  
# def multip(x, y):
#     return x * y
    
# def dividir(x,y):
#     if y == 0:
#         print(" numero B no puede ser 0")
        
#     else:
#         return x / y

# # def repetir():
# #     if input("Quieres repetir (N/Y)? "))

# #MAIN -------------- argumento
# parar = 0
# while parar == False:

# print("""
#     1 - SUMAR
#     2 - RESTAR
#     3 - MULTIPLICAR
#     4 - DIVIDIR  
#       """)

# operacion = int(input("Que operación quieres hacer:"))
# x = int(input("numero A: "))
# y = int(input("numero B: "))


# match operacion:
#     case 1:
#         print(sumar(x,y))
#     case 2:
#         print(restar(x, y))
#     case 3:
#         print(multip(x,y))
#     case 4:
#         print(dividir(x, y))
#     case _:
#         print("no hay esta opcion")


# resultado = add(10, 20)
# print(f"{resultado=}")

# x= 10
# y= 20
# print(f"{x+y=}")

import operMat

if __name__ == "__main__":
#  #   print(operMat.raiz(3))
#     x = int(input("el largo de la superficie: "))
#     y = int(input("el ancho de la superficie: "))
#     print(f"La superficie calculada es: {operMat.multip(x, y)}")  

    print("""
      Hola, tenemos el siguiente menu:
      1. Hamburgesa - 5€
      2. Pizza - 7€
      3. Patatas - 2€
      """)  

def pedidoComida(eleccion):
    IVA = 0.13
    comidas = {"hamburgesa": 5, "pizza": 7, "patatas": 2}
    comida = comidas[eleccion]
    total = comida*(1+IVA)
    return total

print(pedidoComida("pizza"))

# menu = {1: 5, 2: 7, 3:2}
# comida = int(input("Que quieres comer? "))
# cantidad  = int(input("Cuanto quieres? "))

# precio = menu[comida]
# print(f"Sale para pagar {operMat.multip(precio,cantidad)} euros")
