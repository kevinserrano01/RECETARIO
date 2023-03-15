import json
with open("Archivos de datos/recetas.json", 'r') as archivo:
    data = json.load(archivo)

print(type(data))