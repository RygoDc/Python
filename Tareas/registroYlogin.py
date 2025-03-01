"""Programa que simula un registro y login de usuarios
La consola pedira un usuario y una contraseña, 
Tendra que distinguir si existe el usuario o no, y sino preguntara para ver si se quiere crear uno nuevo
en caso de que se registre, se realizara un hash (encriptado) de la contraseña que
quiere meter con doble comprobacion y se guardara en un fichero diccionario JSON 
con el usuario y la contraseña encriptada, en caso de login, se comprobara si el usuario y la contraseña
son correctos"""

import json
import hashlib

def cargarJSON(nombre): #Cargar un archivo JSON
    try:
        with open(nombre, "r") as file: #Abrir el archivo en modo lectura
            return json.load(file) #Cargar el archivo JSON
    except FileNotFoundError: #Si el archivo no existe
        return {} #Devolver un diccionario vacío
    
def guardarJSON(nombre, datos): #Guardar un archivo JSON
    with open(nombre, "w") as file: #Abrir el archivo en modo escritura
        json.dump(datos, file, indent=4) #Guardar el archivo JSON con indentación de 4 espacios

def hashPassword(password): #Función para encriptar una contraseña
    return hashlib.sha256(password.encode()).hexdigest() #Devolver la contraseña encriptada

def registro(diccionario): #Función para registrar un usuario
    usuario = input("Introduce el nombre de usuario: ") #Pedir el nombre de usuario
    if usuario in diccionario: #Si el usuario ya existe
        print("El usuario ya existe") #Mostrar un mensaje
        return #Salir de la función
    password = input("Introduce la contraseña: ") #Pedir la contraseña
    password2 = input("Repite la contraseña: ") #Pedir la contraseña de nuevo
    
    while password != password2: #Si las contraseñas no coinciden
        print("Las contraseñas no coinciden") #Mostrar un mensaje
        password = input("Introduce la contraseña: ")
        password2 = input("Repite la contraseña: ")
        
        
    
    diccionario[usuario] = hashPassword(password) #Añadir el usuario y la contraseña encriptada al diccionario
    guardarJSON("usuarios.json", diccionario) #Guardar el diccionario en un archivo JSON
    print("Usuario registrado") #Mostrar un mensaje

def login(diccionario): #Función para hacer login
    usuario = input("Introduce el nombre de usuario: ") #Pedir el nombre de usuario
    if usuario not in diccionario: #Si el usuario no existe
        print("El usuario no existe") #Mostrar un mensaje
        return #Salir de la función
    password = input("Introduce la contraseña: ") #Pedir la contraseña
    if diccionario[usuario] == hashPassword(password): #Si la contraseña es correcta
        print("Login correcto") #Mostrar un mensaje
    else: #Si la contraseña es incorrecta
        print("Contraseña incorrecta") #Mostrar un mensaje

seguir = True
while seguir:
    usuarios = cargarJSON("usuarios.json") #Cargar el archivo JSON
    opcion = input("¿Quieres hacer login o registro? (login/registro): ") #Pedir
    if opcion == "login": #Si la opción es login
        login(usuarios) #Hacer login
    elif opcion == "registro": #Si la opción es registro
        registro(usuarios) #Hacer registro
    else: #Si la opción no es ni login ni registro
        print("Opción incorrecta") #Mostrar un mensaje
    seguir = input("¿Quieres seguir? (s/n): ") == "s" #Preguntar si se quiere seguir
print("Fin del programa") #Mostrar un mensaje
