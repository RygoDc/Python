import json
import hashlib
#Cargar y guardar JSON
def cargarJSON(nombre): #Cargar un archivo JSON
    try:
        with open(nombre, "r") as file: #Abrir el archivo en modo lectura
            return json.load(file) #Cargar el archivo JSON
    except FileNotFoundError: #Si el archivo no existe
        return {} #Devolver un diccionario vacío
    
def guardarJSON(nombre, datos): #Guardar un archivo JSON
    with open(nombre, "w") as file: #Abrir el archivo en modo escritura
        json.dump(datos, file, indent=4) #Guardar el archivo JSON con indentación de 4 espacios

receta = cargarJSON("receta.json") #Cargar el archivo JSON
receta["difilcutad"] = "Media" #Añadir una nueva clave al diccionario JSON
guardarJSON("receta.json", receta) #Guardar el archivo JSON
print(receta) #Mostrar el archivo JSON