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

from plyer import notification
import time


notification.notify(title="Hola",
    message="Nos queda 15 minutos", timeout=5)

 
