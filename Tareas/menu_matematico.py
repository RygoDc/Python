"""
Este modulo contiene las funciones que se encargan de mostrar el menu de
1.- calcular si el numeroi que pasas es primo
2.- calcular si el numeroi que pasas es par
3.- calcular si el numero (año) que pasas es bisiesto
"""
def es_primo(numero):
    if numero <1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

def es_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 4 == 0 and año % 100 != 0:
        return True
    return False

def menu():
    print("\nMENU")
    print("1.- calcular si el numero que pasas es primo")
    print("2.- calcular si el numero que pasas es par")
    print("3.- calcular si el numero (año) que pasas es bisiesto")
    print("4.- Salir")
    opcion = int(input("Elige una opcion: "))
    return opcion

continuar = True

while continuar:
    opcion = menu()
    if opcion == 1:
        numero = int(input("Introduce un numero: "))
        if es_primo(numero):
            print(f"El numero {numero} es primo")
        else:
            print(f"El numero {numero} no es primo")
    elif opcion == 2:
        numero = int(input("Introduce un numero: "))
        if es_par(numero):
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} no es par")
    elif opcion == 3:
        ano = int(input("Introduce un año: "))
        if es_bisiesto(ano):
            print(f"El año {ano} es bisiesto")
        else:
            print(f"El año {ano} no es bisiesto")
    elif opcion == 4:
        continuar = False