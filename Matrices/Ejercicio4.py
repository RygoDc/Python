"""4. Se captura por teclado los valores de una matriz de 4 x 4. Deseamos saber si es una
matriz identidad. Es aquella que en la diagonal posee el valor 1 y en el resto de las
posiciones tiene el valor 0."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(4):
    tabla.append([])
    for j in range(4):
        tabla[i].append(int(input("Introduce un número: ")))

p(tabla)

identidad = True
for i in range(4):
    for j in range(4):
        if i==j and tabla[i][j]!=1:
            identidad = False
        elif i!=j and tabla[i][j]!=0:
            identidad = False
if identidad:
    print("Es una matriz identidad")
else:
    print("No es una matriz identidad")

