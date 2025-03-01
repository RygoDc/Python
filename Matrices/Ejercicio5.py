"""5.- Diseñar programa Java, que:
a) Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
b) Carga la tabla con valores numéricos enteros.
c) Suma todos los elementos de cada fila y todos los elementos de cada columna
visualizando los resultados en pantalla."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(5):
    tabla.append([])
    for j in range(5):
        tabla[i].append(int(input("Introduce un número: ")))
                        
p(tabla)

suma_filas = []
suma_columnas = []
for i in range(5):
    suma_filas.append(sum(tabla[i]))
    suma_columnas.append(sum([tabla[j][i] for j in range(5)]))

print("Suma de las filas: ",suma_filas)
print("Suma de las columnas: ",suma_columnas)