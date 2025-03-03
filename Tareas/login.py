"""Programa que simula un registro y login de usuarios
La consola pedira un usuario y una contraseña, 
Tendra que distinguir si existe el usuario o no, y sino preguntara para ver si se quiere crear uno nuevo
en caso de que se registre, se realizara un hash (encriptado) de la contraseña que
quiere meter con doble comprobacion y se guardara en un fichero diccionario JSON 
con el usuario y la contraseña encriptada, en caso de login, se comprobara si el usuario y la contraseña
son correctos"""

import json
import hashlib
import pandas as pd
import openpyxl

def cargarJSON(archivo):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def guardarJSON(archivo, datos):
    try:
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
    except FileNotFoundError:
        print("Error al guardar el archivo")

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def guardarExcel(datos):
    cont = 1
    nombreUsuarios = []
    contrasenas = []
    for usuario in datos:
        nombreUsuarios.append(datos[usuario])
        contrasenas.append(usuario)
        cont += 1
    df = pd.DataFrame({
        "Usuario": contrasenas,
        "Contraseña": nombreUsuarios
    })
    df.to_excel("todosLosUsuarios.xlsx")

def registro(diccionario):
    usuario = input("Introduce el nombre de usuario: ")
    if usuario in diccionario:
        print("El usuario ya existe")
        return
    password = input("Introduce la contraseña: ")
    password2 = input("Repite la contraseña: ")

    while password != password2:
        print("Las contraseñas no coinciden")
        password = input("Introduce la contraseña: ")
        password2 = input("Repite la contraseña: ")

    diccionario[usuario] = hashPassword(password)
    guardarJSON("usuarios.json", diccionario)
    guardarExcel(diccionario)       
    print("Usuario registrado")

def login(diccionario):
    usuario = input("Introduce el nombre de usuario: ")
    if usuario not in diccionario:
        print("El usuario no existe")
        print("¿Quieres registrarte?")
        respuesta = input("s/n: ")
        if respuesta.lower() == "s":
            registro(diccionario)            
        return
    password = input("Introduce la contraseña: ")
    if diccionario[usuario] == hashPassword(password):
        print("Login correcto")
    else:
        print("Contraseña incorrecta")

seguir = True
while seguir:
    usuarios = cargarJSON("usuarios.json")
    opcion = input("¿Quieres hacer login o registro? (login/registro): ")
    if opcion.lower() == "login":
        login(usuarios)
    elif opcion.lower() == "registro":
        registro(usuarios)
    else:
        print("Opción no válida")    
    seguir = input("¿Quieres seguir? (s/n): ").lower() == "s"
