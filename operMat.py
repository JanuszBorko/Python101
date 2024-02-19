def sumar(x, y):
    return x + y
    
def restar(x, y):
    return x - y
  
def multip(x, y):
    return x * y
    
def dividir(x,y):
    if y == 0:
        print(" numero B no puede ser 0")
        
    else:
        return x / y
    

if __name__ == "__main__":   # solo ejecutable en fichero donde se ejecuta
    print(dividir(8,2))