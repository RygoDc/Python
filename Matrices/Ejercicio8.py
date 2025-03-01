"""Una vez cargado un array numérico de dos dimensiones (10X15), obtener un array
unidimensional o vector cuyo primer elemento contenga la suma de los elementos de
la primera fila del array bidimensional, el segundo la suma de los elementos de la
segunda fila del array bidimensional, y así sucesivamente."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(10):
    tabla.append([])
    for j in range(15):
        tabla[i].append(int(input("Introduce un número: ")))

p(tabla)

suma_filas = [sum(tabla[i]) for i in range(10)]
print("Suma de las filas: ",suma_filas)