'''
COMO usuario de datos bancarios
QUIERO introducir numeros de las transacciones bancarias hasta 
que el usuario no tenga más. 
Al final, mostrar un informe del total de los
numeros introducidos y la media
PARA que cumplamos con las normativa bancaria

'''

1-- Añadir dinero
2-- Retirar dinero
3-- Ver saldo
0-- Salir

while action != 0:
    match action:
        case "1":
            saldo = float(input("Cuanto dinero quieres añadir: "))
        case "2":
            
            
