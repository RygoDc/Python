"""Crear una tabla de dos dimensiones, cuyo contenido serán las potencias de 2. La
primera columna de la tabla nos indicara el exponente (positivo o negativo) y la
segunda columna su valor.
El tamaño de la tabla será 20x2.
Se pedirá que el usuario introduzca los valores de las potencias que quiere visualizar
hasta que al introducir la potencia se introduzca un -1000."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(20):
    tabla.append([])
    tabla[i].append(int(input("Introduce un número: ")))
    if tabla[i][0]==-1000:
        break
    tabla[i].append(2**tabla[i][0])

p(tabla)

