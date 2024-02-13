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

# s = "hola,Agur,Hi,Gye,goodbye"
# res = s.split(",")
# copy = res
# print(res)
# print(copy)

# matriz = {}
# for i in res:
#     for j in copy:
#         matriz.update({j:i})
# print(matriz)


# texto = "   programazioa gustatzen gustatzen   zait.  "
# #print("X"+ texto.strip() + "X")
# texto = "X"+ texto.replace("  ","") + "X"
# print("X"+ texto.replace("  ","") + "X")
# print(texto.count("gustatzen"))
# y = len(texto)
# print(texto[len(texto)-6:])
# print(texto[-6:])


# s="    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "
# s = s.strip()
# x= s.split(",")
# listaDePalabras = []
# for i in x:
#     if not i.isnumeric():
#         print(i,"", end="")
#         listaDePalabras.append(i)

# resultado = " ".join(listaDePalabras)
# print(resultado.upper())
# print(resultado.title())


# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
# texto = texto.replace("Bill Gates", "Guido Van Rossum")
# texto = texto.replace("difícil","facil").replace("Pitón","Python")
# print(texto)


texto = """    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas 
importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es 
facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 
'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. 
Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, 
si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. 
Y eso hace que mi vida sea mucho más fácil        """

print(texto.upper().count("PYTHON"))
print(texto.upper().find("PYTHON"))
print(texto[texto.upper().find("PYTHON")+1:].upper().find("PYTHON"))
