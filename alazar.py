<<<<<<< HEAD
import random
# print(random.random())
# print(random.randint(1,26))

lista = {"lunes":0,"martes":0,"miercoles":0,"jueves":0,"viernes":0}
valores = list(lista.keys())
print(valores)
for x in range(100000):
    dia = random.choice(valores)
    contador = int(lista.get(dia)) +1
    lista.update({dia:contador})
print(lista)
suma = 0
for y in lista.values():
    suma = suma + y
=======
import random
# print(random.random())
# print(random.randint(1,26))

lista = {"lunes":0,"martes":0,"miercoles":0,"jueves":0,"viernes":0}
valores = list(lista.keys())
print(valores)
for x in range(100000):
    dia = random.choice(valores)
    contador = int(lista.get(dia)) +1
    lista.update({dia:contador})
print(lista)
suma = 0
for y in lista.values():
    suma = suma + y
>>>>>>> ec36c0a444f02d26751d785df8e4b6626bedad40
print(suma)