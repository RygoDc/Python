"""Visualizar la matriz transpuesta de la anterior. Si la matriz es cuadrada (tiene igual
número de filas y de columnas) visualice también los elementos de la diagonal
principal.
"""
from printMatriz import printMatrix

tabla =[[3,2,5,0,9],[9,10,2,3,1],[-3,2,3,43,1]]
tabla_traspuesta = []


for i in range(len(tabla[0])):
    tabla_traspuesta.append([])
    for j in range(len(tabla)):
        tabla_traspuesta[i].append(tabla[j][i])

printMatrix(tabla)
print("\n")
printMatrix(tabla_traspuesta)