import os

#Verificar si es un directorio o un fichero
if os.path.isdir("fichero.txt"):
    print("Es Directorio")

if os.path.isfile("fichero.txt"):
    print("Es fichero")

#Verificar si existe el fichero, si no existe lo crea
if os.path.exists("fichero.txt"):
    print("Existe")
    f = open("fichero.txt","a") #a -> append
    f.write("Hola. \n") #write -> escribir 
else:
    print("No existe")
    f = open("fichero.txt", "x") #x -> create

f.close() #Cerrar el fichero