"""
COMO un programador de videojuegos,
QUIERO desarrollar un programa para que el usuario adivine un numero
PARA mostrarlo como prototipo de videojuego
creado en python
"""

x = 23

print("LET THE GAME BEGIN!! \n")
resultado = False
i = 1
n = 5
while resultado == False:
    y = int(input(f"Que numero tengo en mi mente:"))
    if x == y:
        resultado = True
        print(f"\nCONGRATULATIONS!!!\n{y} es el numero que buscamos. Lo has adivinado en {i} pruebas")
   
    elif (y > x) and (i<n):
        print(f"Numero es MAYOR del buscado!! Prueba otra vez. Te quedan {n-i} intentos\n")
        i = i+1
   
    elif (y < x) and (i<n):
        print(f"Numero es MENOR del buscado!! Prueba otra vez. Te quedan {n-i} intentos\n")
        i = i+1
   
    else:
        print("GAME OVER\nYou lost!!")
        resultado = True
