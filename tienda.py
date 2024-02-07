'''
Gestión de una tienda
Se podría extender la idea de arriba para crear una aplicación para gestionar la compra de productos en una tienda.

“Bienvenidos a mi tienda. Hoy tenemos especiales de:
manzanas
zumos
leche

Introducir “1” para ver todos los productos, “2” para hacer una compra…”, “3” para borrar un producto, …

Al introducir “2”, mostrar el precio (igual para todos, excepto los productos especiales - % menos) y pedir al usuario dinero (por ejemplo, te dará 20 euros). Dáslo el producto al usuario y la diferencia de dinero (lo que te ha dado menos el coste).

'''


productos = [['manzanas', 2.50], ['zumos', 1.3], ['leche', 1.9], ['galletas', 3.4]]
accion = int(input('Bienvenidos en la Tienda TU TIENDA DEL E-BARRIO. \n\nPara seguir pulsa:\n“1” para ver todos los productos, \n“2” para hacer una compra, \n“3” para borrar un producto \n'))

if accion == 1:
    print('Tenemos los siguientes productos disponibles:')
    for i in range(len(productos)):
        print(f'{i+1}. {productos[i][0]} a {productos[i][1]} €')
elif accion == 2:
    otraCompra = "s"
    while otraCompra == "s":

        print('Tenemos los siguientes productos disponibles:')
        for i in range(len(productos)):
            print(f'{i+1}. {productos[i][0]} a {productos[i][1]} €')

        compra = int(input('\nQue producto quieres comprar de la lista: '))
        cantidad = int(input('Cuantas unidades quieres comprar: '))
        importe = productos[compra-1][1]*cantidad
        print(f'Importe a pagar es :{importe:.2f}')
        pago = float(input('Cuanto pagas: '))
        ex = 0
        if pago < importe:
            while pago < importe:
                ex = float(input(f'\nImporte pagado es menor de debido. Caunto más vas a pagar: '))
                pago = pago + ex 
                print(f'Tu vuelta son {(pago - importe):.2f}')
        else:
            print(f'Tu vuelta son {(pago - importe):.2f}.')
        otraCompra = input(f'\nNecesitas algo más (s/n)? ')

    print('\n\nMUCHAS GRACIAS POR TU VISITA')
elif accion == 3:
    pass
else :
    print('Esta opcion no es valida')

    print("FIN")
