'''
COMO usuario de datos bancarios
QUIERO introducir numeros de las transacciones bancarias hasta 
que el usuario no tenga más. 
Al final, mostrar un informe del total de los
numeros introducidos y la media
PARA que cumplamos con las normativa bancaria

'''
'''
1-- Añadir dinero
2-- Retirar dinero
3-- Ver saldo
0-- Salir
'''

action= 1
saldo = 0
while action != "0":
    match action:
        case "1":
            saldo = saldo + float(input("Cuanto dinero quieres añadir: "))
            action = input("Que quieres hacer ahora? ")
        case "3":
            print(f"Tu saldo es de {saldo} €")
            action = 4
        case _:
            print("1-- Añadir dinero \n2-- Retirar dinero \n3-- Ver saldo \n0-- Salir")
            action = input("Que accion quieres hacer: ")

            