"""6.- Cargar desde teclado un array con las notas de las 3 asignaturas de cada uno de los 15
alumnos de una clase. Cada fila contendrá los datos de una asignatura y cada columna
la nota de un alumno determinado. Visualizar la nota media de cada alumno, la nota
media de cada asignatura y la nota media de la clase."""

from printMatriz import printMatrix

p = printMatrix

tabla = []
for i in range(3):
    tabla.append([])
    for j in range(15):
        tabla[i].append(int(input("Introduce la nota del alumno "+str(j+1)+" en la asignatura "+str(i+1)+": ")))

p(tabla)

media_alumnos = [sum(tabla[i])/15 for i in range(3)]
media_asignaturas = [sum([tabla[j][i] for j in range(3)])/3 for i in range(15)]
media_clase = sum([sum(tabla[i]) for i in range(3)])/45

print("Media de los alumnos: ",media_alumnos)
print("Media de las asignaturas: ",media_asignaturas)
print("Media de la clase: ",media_clase)

