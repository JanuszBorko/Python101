# import math as m

# x = 5.75
# print(m.ceil(x))


# from math import ceil, floor   # para optimizar el codigo

# x = 5.75
# print(ceil(x))



import random
# print(random.random())
# print(random.randint(1,26))

lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
for x in range(100000):
    dia = random.choice(lista)
    print(lista.count(dia))



    
   
