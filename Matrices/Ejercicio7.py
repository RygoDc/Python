"""Realizar un programa que:
a. Llene un array bidimensional con las notas numéricas de cada estudiante en las
clases de un profesor, se supone que el profesor tiene 3 clases diferentes y un
máximo de 30 alumnos por clase.
b. Visualice el array.
c. Calcule la nota máxima y mínima visualizando a que alumno y grupo pertenece, en
caso de que estas notas se repitan se visualizan todas"""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(3):
    tabla.append([])
    for j in range(30):
        tabla[i].append(int(input("Introduce la nota del alumno "+str(j+1)+" en la clase "+str(i+1)+": ")))

p(tabla)

maximo = max([max(tabla[i]) for i in range(3)])
minimo = min([min(tabla[i]) for i in range(3)]) 
maximos = []
minimos = []
for i in range(3):
    for j in range(30):
        if tabla[i][j]==maximo:
            maximos.append((i,j))
        if tabla[i][j]==minimo:
            minimos.append((i,j))
print("Nota máxima: ",maximo," en los alumnos: ",maximos)
print("Nota mínima: ",minimo," en los alumnos: ",minimos)

