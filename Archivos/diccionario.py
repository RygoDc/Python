import json
#Cargar un archivo JSON en un diccionario
with open("receta.json", "r") as fichero: #Abrir el archivo en modo lectura
    datos = json.load(fichero) #Cargar el archivo JSON en un diccionario

print(datos["tiepoPreparacion"]) #Mostrar el tiempo de preparación

for ingrediente in datos["ingredientes"]: #Recorrer la lista de ingredientes
    print(ingrediente) #Mostrar cada ingrediente
    if ingrediente["nombre"] == "harina": #Si el ingrediente es harina
        print("Habrá bechamel") #Mostrar un mensaje

print(datos) #Mostrar el diccionario JSON