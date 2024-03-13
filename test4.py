# import requests

# r = requests.get('https://cat-fact.herokuapp.com/facts/')
# # print(r.status_code)
# # print(r.text)
# # print(r.json())

# texto = r.json()
# t: list[str]=[]
# for i in texto:
#     # t=t.append(i)
#     # print(i)
#     print(i["text"])

# print("\n")
# print(texto[0]["text"])

# elementos = len(texto)
# print(texto[elementos-2])


# from translate import Translator

# translator = Translator(to_lang="pl", from_lang="de")
# texto = translator.translate("wie geht es dir")
# print(texto)

# from email_validator import validate_email, EmailNotValidError

# email = "januszborko@gmail.com"

# try:
#     emailinfo = validate_email(email, check_deliverability=True)
#     print(emailinfo)
#     email = emailinfo.normalized
#     print(email)
# except EmailNotValidError as e:
#     print(str(e))

# from plyer import notification
# import time


# notification.notify(title="Hola",
#     message="Nos queda 15 minutos", timeout=5)

# import sqlite3

# conn = sqlite3.connect('pelis.db')
# conn.execute('CREATE TABLE Empleados (id integer, nombre text, salario float)')

# conn.close()
 
# frutas = ['MANZAS', 'pera', 'NARANJA', 'uva', 'MELON']
# # nueva_fruta= []

# # for fruta in frutas:
# #     if fruta.isupper():
# #         nueva_fruta.append(fruta)

# # print(nueva_fruta)

# print([fruta for fruta in frutas if fruta.isupper()])

# numeros = [2,6,7,3,4,8]
# print(["par" if numero%2 == 0 else "inpar" for numero in numeros])

# def sumar(x, y):
#     return x+y

# z = sumar(3, 2)
# print(z)

# sumar = lambda x, y: x + y

# print(sumar(10, 5))

# print((lambda x, y: x + y)(10, 1))

# up = lambda s: s.upper()
# print(up("hola"))

# hola = lambda s: "kaixo "+s

# print(hola("Jon"))

# par = lambda s: "par" if s%2==0 else "inpar" 

# s= [1,2,3,4,5]
# for _ in s:
#     print(par(_), end=" ")

# print()
# sign = lambda x: "negat" if x<0 else "posit"   
# s= [-1,2,-3,4,-5]
# for _ in s:
#     print(sign(_), end=" ")

# productos = ["raqueta", "balon", "guantes", "pelota"]

# up = [product.capitalize() for product in productos]

# for _ in up:     
#     print(_)

# def convertir_may(s):
#     return s.capitalize()  

# print(list(map(convertir_may, productos)))  #map es una forma de bucle en un una linea
# print(list(map(lambda s: s.capitalize(), productos))) 

import math

lista = [4,5,6]
lista2 = [1,2,3]
lista3 = [7,8,9]
print(list(map(lambda s: s+2, lista)))
print(list(map(lambda s: math.sqrt(s), lista)))
print(list(map(lambda x, y, z: x*y*z, lista, lista2, lista3)))
