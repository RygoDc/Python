







def printMenu():
    return (
        "1.- calcular si el numero que pasas es primo\n"
        "2.- calcular si el numero que pasas es par\n"
        "3.- calcular si el numero (año) que pasas es bisiesto\n"
        "4.- Salir\n"
    )

def elegirOpcion():
    eleccion= input(printMenu())
    while eleccion not in "1234":
        eleccion= input(printMenu())
    return eleccion

def esPar(numero):
    return numero % 2 == 0

def esPrimo(numero):
    if(numero == 1 or numero % 2 == 0):
        return False