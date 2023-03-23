import json
import datetime as time

def mostrar_receta(obj, indice):
    """Funcion que se va a ejecutar cuando el usuario clickee en un boton que tenga el command=mostrar_receta"""
    print(f"Nombre: {obj['recetas'][indice]['nombre']}")
    print("Ingredientes:")
    ingredientes = obj['recetas'][indice]['ingredientes']
    for ingrediente in ingredientes:
        print(f"- {ingrediente['nombre']}: {ingrediente['cantidad']} {ingrediente['unidad']}")
    print("Preparación:")
    pasos = obj['recetas'][indice]['preparacion']
    i = 1
    for paso in pasos:
        print(f"paso {i} - {paso}")
        i += 1
    print(f"Tiempo de preparación: {obj['recetas'][indice]['tiempo_preparacion']} minutos")
    print(f"Tiempo de cocción: {obj['recetas'][indice]['tiempo_coccion']} minutos")
    # print(f"Fecha de creación: {obj['recetas'][indice]['fecha_creacion']}")
    fecha = time.datetime.now() # guardamos le fecha y hora actual de nuestra PC
    print(f"Fecha de creación: {fecha.strftime('%Y-%m-%d Hora: %H:%M:%S')}") # usar para la creacion de receta
    print(f"Etiquetas: {', '.join(obj['recetas'][indice]['etiquetas'])}")
    es_favorita = obj['recetas'][indice]['favorita']
    print(f"Es favorita: {'Sí' if es_favorita else 'No'}")
    if obj['recetas'][indice]['imagen']:
        print("Imagen:")
        print(f"- {obj['recetas'][indice]['imagen']}")

def cargar_receta():
    pass

def eliminar_receta():
    pass

def modificar_receta():
    pass

def tomarDatos():
    with open('./Archivos de datos/recetas.json', 'r') as file:
        return json.load(file)
    
     
    
# Leemos el archivo JSON y guardamos sus datos en la variable 'data' para manipularlo
with open('./Archivos de datos/recetas.json', 'r') as file:
    data = json.load(file)

# Creamos un mini menu para que seleccione el usuario que receta quiere ver.
# print('Menu: \n0- Pastel de chocolate \n1- Arroz con pollo')
# op = int(input('Ingrese una opcion: '))

# llamamos a la funcion y le pasamos por parametro el objeto con su indice elegido por el usuario
# mostrar_receta(data, op)
