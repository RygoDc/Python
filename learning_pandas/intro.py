import pandas as pd
import json
import openpyxl



animalId = []
animalName = []
animalType = []
animalArrivalDate = []

def loadJSON():
    try:
        with open('animales.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


animalesCall = loadJSON()
animales = animalesCall["animales"]



cont = 1
for animal in animales:
    animalId.append(cont)
    animalName.append(animal["nombre"])
    animalType.append(animal["especie"])
    animalArrivalDate.append(animal["fecha_llegada"])
    cont += 1

df = pd.DataFrame({
    "Número": animalId,
    "Nombre": animalName,
    "Especie": animalType,
    "Fecha de llegada": animalArrivalDate
})

print(df)

df = df.sort_values(by="Especie")
print(df)

df.to_excel("animalitos.xlsx")
