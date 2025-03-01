"""1. Hacer un programa, que:
a) b) Crea una matriz de 10x10 (filas x columnas) y nombre 'tabla'.
Carga la matriz de manera que las filas pares se rellenan con 1 y las filas impares
con 0.
c) Una vez inicializada la matriz muestra su contenido en pantalla."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(10):
    tabla.append([])
    for j in range(10):
        if i%2==0:
            tabla[i].append(1)
        else:
            tabla[i].append(0)
        
p(tabla)