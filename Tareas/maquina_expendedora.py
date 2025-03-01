"""
Maquina expendedora de bebidas
agua 0.50 euros
refresco 0.75 euro
zumo 0.95 euros

El programa emitira un menu que mostrara productos y precios, ademas de la opcion de salir
pedira la opcion elegida y pedira monedas al usuario

la maquina acepta todas las monedas de 2 euros a 5 centimos

Al comienzo del dia se dispondra de 20 monedas de cada tipo

se debe dar el cambio correcto, con el menos numero de monedas posibles
la maquina mostrara un mensade de INTRODUZCA IMPORTE EXACTO en caso de no tener 2 tipos de moneda cualesquiera o
si una de las ausentes es la pila de 5 centimos, solo aceptara el importe exacto en este caso

al final del programa nos debe dar el total de nimero disponible en la maquina, por unidad monetaria
"""

valoresMonedas= [2, 1, 0.50, 0.20, 0.10, 0.05]
reservaMonedas = [20, 20, 20, 20, 20, 20]

productos = ["agua 💧", "refresco 🥤", "zumo 🧃"]
precios = [0.50, 0.75, 0.95]

def ingreso_monedas():
    monedas_suficientes = True
    contador =0.0
    monedas_ingresadas = []
    while monedas_suficientes:
        moneda = float(input("Ingrese moneda: "))
        if moneda in valoresMonedas:
            contador += moneda
            monedas_ingresadas += [moneda]                
            if contador >= precios[opcion-1]:
                monedas_suficientes = False
                print(f"Total: {contador}")
                print(f"Monedas ingresadas: {monedas_ingresadas}")                                                         
            else:
                print(f"Faltan {(precios[opcion-1]-contador):.2f} euros")
        else:
            print("Moneda no valida")

    return monedas_ingresadas

def devolver_monedas(cambio):
    monedas_devueltas = []
    for valor in valoresMonedas:
        while cambio >= valor and reservaMonedas[valoresMonedas.index(valor)] > 0:
            cambio = round(cambio - valor, 2)
            monedas_devueltas.append(valor)
    if cambio > 0:
        print("No hay suficiente cambio disponible. Por favor ingrese el importe exacto.")
        return []
    return monedas_devueltas

    
def agregar_monedas(paso1):
    for moneda in paso1:
        reservaMonedas[valoresMonedas.index(moneda)] += 1
    return reservaMonedas

def quitar_monedas(paso3):
    for moneda in paso3:
        reservaMonedas[valoresMonedas.index(moneda)] -=1
    return reservaMonedas

def calculo_dinero():
    dinero = 0
    for i in range(len(valoresMonedas)):
        dinero += valoresMonedas[i] * reservaMonedas[i]       
    return dinero

def comprobando_repos():
    contador = 0
    if contador == len(reservaMonedas):
        print("No hay monedas disponibles en la maquina")
    for i in range(len(reservaMonedas)):
        if reservaMonedas[i] == 0:
            print(f"El repositorio de la moneda {valoresMonedas[i]} esta vacio")
            contador +=1
    if contador == 2 or reservaMonedas[valoresMonedas.index(0.5)]==0:
            print("INTRODUZCA IMPORTE EXACTO")

def menu():
    print("\nMENU")
    for i in range(len(productos)):
        print(f"{i+1} - {productos[i]} - {precios[i]} euros")
    print("4 - Salir")
    opcion = int(input("\nElige una opcion: "))
    return opcion

continuar = True

while continuar:
    opcion = menu()
    if opcion == 4:
        continuar = False
    else:        
        comprobando_repos()
        print(f"Dinero disponible: {calculo_dinero()} euros")

        print(f"Has elegido {productos[opcion-1]}")
        print(f"El precio es {precios[opcion-1]} euros")
        paso1 = ingreso_monedas()
        paso2 = agregar_monedas(paso1)
        # print(f"Total de monedas disponibles despues del paso 2: {reservaMonedas}")

        cambio = round(sum(paso1) - precios[opcion-1], 2)
        if cambio == 0:
            print("Gracias por su compra")
        else:
            print(f"Su cambio es {cambio} euros")

        paso3 = devolver_monedas(cambio)        
        print(f"Monedas a devolver: {paso3}")

        paso4 = quitar_monedas(paso3)
        # print(f"Total de monedas disponibles despues del paso 4: {reservaMonedas}")

        # print(f"Monedas: {valoresMonedas}")
        # print(f"Total de monedas disponibles: {reservaMonedas}")

        print(f"Dinero disponible en la maquina:  {calculo_dinero()} euros")


