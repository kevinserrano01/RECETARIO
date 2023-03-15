import datetime
import json
nombre = 'Risotto de Cabalaza'
ingredientes = [{'nombre': 'arroz','cantidad': 150,'UnidadMedida':'gr' },{'nombre':'Calabaza' ,'cantidad':200 ,'UnidadMedida':'gr' },{'nombre': 'cebolla','cantidad': 1,'UnidadMedida':'unidad' },
                {'nombre':'Caldo' ,'cantidad':0.5 ,'UnidadMedida':'litros' },{'nombre': 'vino blanco','cantidad': 1,'UnidadMedida':'vaso' },{'nombre':'manteca' ,'cantidad':1 ,'UnidadMedida': 'cucharita'},
                {'nombre':'Queso parmesano' ,'cantidad': 30,'UnidadMedida':'gr' },{'nombre': 'Sal','cantidad':1 ,'UnidadMedida':'cucharita'},{'nombre': 'Pimienta','cantidad': 1,'UnidadMedida': 'cucharita'}]
pasos = ['paso 1', 'paso 2', 'paso 3', 'paso 4', 'paso 5', 'paso 6']
imagen = ""
preparacion = 60
coccion = 30
fecha_creacion = f'{datetime.datetime.day}/{datetime.datetime.month}/{datetime.datetime.year}'
etiquetas = ['Risotto', 'Calabaza']
favorita = True

receta={'nombre': nombre, 'ingredientes':ingredientes, 'pasos': pasos,
        'preparacion':preparacion, 'coccion':coccion, 'fecha_creacion':fecha_creacion,
        'etiquetas':etiquetas, 'favorita':favorita}

with open('recetas.json', 'w') as archivo:
    json.dump(receta, archivo)

def funcion():
        pass