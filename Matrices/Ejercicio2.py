"""Diseñar programa Java, que:
a) Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
b) Carga la tabla de forma que los componentes pertenecientes a la diagonal
principal de la matriz tomen el valor 1 y el resto el valor 0.
c) Muestra el contenido de la tabla en pantalla."""
from printMatriz import printMatrix

p= printMatrix

tabla = []
for i in range(5):
    tabla.append([])
    for j in range(5):
        if i==j:
            tabla[i].append(1)
        else:
            tabla[i].append(0)
        
p(tabla)