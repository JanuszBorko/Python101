# import datetime 

# print(datetime.datetime.now())


# import datetime 

# hoy = datetime.datetime.now()

# print(hoy.day)
# print(hoy.month)
# print(hoy.microsecond)

# s = datetime.datetime.strptime("2012/01/17", "%Y/%m/%d")

# print(s + datetime.timedelta(days=100))
# datetime.datetime.strptime()


# import webbrowser
# webbrowser.open("http://www.google.com")
                        
# paises = {"Australia":"Canberra", "España":"Madrid"}
#print(type(paises))
#print(paises["Australia"])  # igual funcion que get() salvo los parentesis

# paises.update({"España":"Bilbao"})
# print(paises.get("España"))
# paises.update({"Mexico":"Mexico DF"})
#print(paises.get("Mexico"))
#paises.pop("España")
# print(paises)
# x = paises.popitem()
# print(paises)
# print(x)


# for k, v in paises.items():
#     print(k, v)

# for k in paises.items():
#     print(k)

# for v in paises.keys():
#     print(v)

# for z in paises.values():
#     print(z)


# user1 = {"email":"che@g.com", "nombre":"Che"}       #!!!!! gestion de usuarios
# user2 = {"email":"maria@g.com", "nombre":"Maria"}

# users = [user1, user2]

# for i in users:
#     print(i["nombre"])


# coche1 = {"marca":"Ford", "modelo":"Cougar", "motor":"2.0 V6"}
# coche2 = {"marca":"Ford", "modelo":"k2", "motor":"1.1 V3"}

# coche1.update({"variante":"coupe"})

# coleccion = [coche1, coche2]

# print(coleccion)

# listaComidas = {}
# for i in range(3):
#     nombre = input("Cual es tu nombre: ")
#     comida = input("Que comida te gusta: ")
#     listaComidas.update({nombre:comida})

# for k, v in listaComidas.items():
#     print(f"{k} ha comido {v}")


# s = "hola Agur Hi Gye goodbye"

# print(s.upper())
# s= s.capitalize()
# # s = s.replace("agur", "aaaaa")
# i = s.find("hi")
# print(s[i:])

# if "HOLA" in s.upper():
#     print("si")

s = "hola,Agur,Hi,Gye,goodbye"
res = s.split(",")
copy = res
print(res)
print(copy)

matriz = {}
for i in res:
    for j in copy:
        matriz.update({j:i})
print(matriz)