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

numeros = [2,6,7,3,4,8]
print(["par" if numero%2 == 0 else "inpar" for numero in numeros])
