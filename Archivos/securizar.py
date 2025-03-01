import hashlib

#Cifrado de contraseñas con SHA-256
password="nombreDelPerro123" #Contraseña a cifrar
hash = hashlib.sha256(password.encode()).hexdigest() #Cifrar la contraseña

print(password) #Mostrar la contraseña
print(hash) #Mostrar la contraseña cifrada


