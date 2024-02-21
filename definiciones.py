from datetime import datetime

def km_milas(km:float):   #el resultado como int
    """             
        Este funcion es para convertir km a milas
        Parametros: kilometros
    """
    mila = km * 0.62137
    return mila

def adulto(edad:int)->bool:
    """             
        Este funcion es para calcular la edad adulta en base de la fecha de nacimiento
        Parametros: fecha nacimiento
    """
    if edad < 18:
        return False
    else:
        return True

    # fecha = datetime.date() - datetime.date(1984,6,22)
    # return fecha

def mayuscula(s:str)->bool:
    if s[0] == s[0].upper():
        return True
    else:
        return False

def calc(*args, **kwargs):
    for k, v in kwargs.items():
        print(k,v)


def pares(numero:int):
    """
    funcion para comprobar numeros si son pares o inpares
    variables: numero a testear
    resultado: true si es par
    """
    
    if numero % 2 == 0:
        return "El numero es par"
    else:
        return "El numero is impar"

def maximo(*args):
    max = float('-inf')
    for i in args:
        if i> max:
            max = i
        else:
            pass
    return max

def minmax(*args):
    return min(args), max(args)

# def adultos(birthdate):
#     today = datetime.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     if age < 18:
#         return False
#     else:
#         return True

#------------MAIN--------------

# km = float(input("Cuantas km conviertes: "))
# print(f"{km:.1f} son iguales a {km_milas(km):.2f} milas

# edad = int(input("Cual es tu edad? "))

# print(adulto(edad))

# texto = input("Tu texto")
# print(mayuscula(texto))

# calc(err=10, rere=15, kker="kfskd")

# x= int(input("Dime el numero: "))
# # if pares(x):
# #     print(f'Numero {x} es PAR')
# # else:
# #     print(f'Numero {x} es INPAR')

# print(pares(x))

print(minmax(-2, 0 ,-45, -6, -23))



# dictionario 
print("test")