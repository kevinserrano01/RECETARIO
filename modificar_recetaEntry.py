import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from datetime import datetime 

class App(ttk.Frame):
    def __init__(self, parent, ruta, nombre):
        super().__init__(parent, padding=(10))
        self.parent = parent # referencia a la ventana ppal
        parent.configure(bg='black')
        parent.title("MODIFICAR RECETA")
        # parent.resizable(False, False)
        self.ruta= ruta
        self.nombreModificar = nombre
        
        data = self._read()
        for receta in data:
            if receta['nombre'] == self.nombreModificar:
                self.receta = receta
                
        # variables de datos a guardar
        self.nombre = tk.StringVar()
        self.nombre.set(self.receta['nombre'])
        self.ingredientes = tk.StringVar()
        self.pasos = tk.StringVar()
        self.preparacion = tk.StringVar()
        self.preparacion.set(self.receta['tiempo_preparacion'])
        self.coccion = tk.StringVar()
        self.coccion.set(self.receta['tiempo_coccion'])
        self.etiquetas = tk.StringVar()
        self.fav = tk.BooleanVar()
        #seteo del checkbox para que aparezca segun diga en el JSON
        if self.receta['favorita'] == 'true':
            self.fav.set(True)
        else:
            self.fav.set(False)
        
                
        #obtencion de listas para los combobox
        self.listaIngredientes = ['Seleccione un Ingrediente']
        self.listaPasos = ['Seleccione un paso']
        self.listaEtiquetas = ['Seleccione una etiqueta']

        for ingrediente in self.receta['ingredientes']:
            opcion = f"{ingrediente['nombre']}: {ingrediente['cantidad']} {ingrediente['unidad']}"
            self.listaIngredientes.append(opcion)
            
        for paso in self.receta['preparacion']:
            self.listaPasos.append(paso)
            
        for etiqueta in self.receta['etiquetas']:
            self.listaEtiquetas.append(etiqueta)

        ttk.Label(self.parent, text="Modifique cada campo con la data que quiera.",bootstyle="inverse-dark", padding=3).grid(row=0, column=1, columnspan=2)
        
        # nombre
        ttk.Label(self.parent, text="Nombre: ", bootstyle="inverse-dark", padding=3).grid(row=1, column=1)
        ttk.Entry(self.parent, textvariable=self.nombre, bootstyle="primary").grid(row=1, column=2)
        
        # ingredientes
        ttk.Label(self.parent, text="Ingredientes: ", bootstyle="inverse-dark", padding=3).grid(row=2, column=1)
        # ttk.Entry(self.parent, textvariable=self.ingredientes).grid(row=2, column=2)
        self.comboIngredientes = ttk.Combobox(self.parent, textvariable=self.ingredientes, values=self.listaIngredientes, state="readonly")
        #, state="readonly"
        self.comboIngredientes.grid(row=2, column=2, ipadx=20)
        self.comboIngredientes.current(0)
        
        self.ingredienteNuevo = tk.StringVar()
        ttk.Label(self.parent, text="->", bootstyle="inverse-dark",padding=3).grid(row=2, column=3)
        ttk.Entry(self.parent, textvariable=self.ingredienteNuevo, bootstyle="primary").grid(row=2, column=4, padx=5)
        
        # pasos de preparacion
        ttk.Label(self.parent, text="Seleccionar un paso y modificarlo: ", bootstyle="inverse-dark", padding=3).grid(row=3, column=1)
        # ttk.Entry(self.parent,textvariable=self.pasos).grid(row=3, column=2)
        self.comboPasos = ttk.Combobox(self.parent, textvariable=self.pasos, values=self.listaPasos, state="readonly")
        #, state="readonly"
        self.comboPasos.grid(row=3, column=2, ipadx=20)
        self.comboPasos.current(0)
        
        self.pasoNuevo = tk.StringVar()
        ttk.Label(self.parent, text="->", bootstyle="inverse-dark", padding=3).grid(row=3, column=3)
        ttk.Entry(self.parent, textvariable=self.pasoNuevo, bootstyle="primary").grid(row=3, column=4, padx=5)
        
        # tiempo preparacion
        ttk.Label(self.parent, text="Tiempo preparacion (min): ", bootstyle="inverse-dark", padding=3).grid(row=5, column=1)
        ttk.Entry(self.parent,textvariable=self.preparacion, bootstyle="primary").grid(row=5, column=2)
        
        # tiempo de coccion
        ttk.Label(self.parent, text="Tiempo de coccion: ", bootstyle="inverse-dark", padding=3).grid(row=6, column=1)
        ttk.Entry(self.parent,textvariable=self.coccion, bootstyle="primary").grid(row=6, column=2)
        
        # etiquetas
        ttk.Label(self.parent, text="Etiquetas: ", bootstyle="inverse-dark", padding=3).grid(row=7, column=1)
        self.comboEtiquetas = ttk.Combobox(self.parent, textvariable=self.etiquetas, values=self.listaEtiquetas, state="readonly")
        #, state="readonly"
        self.comboEtiquetas.grid(row=7,column=2, ipadx=20)
        self.comboEtiquetas.current(0)
        
        self.etiquetaNueva = tk.StringVar()
        ttk.Label(self.parent, text="->", bootstyle="inverse-dark", ).grid(row=7, column=3, padx=5)
        ttk.Entry(self.parent, textvariable=self.etiquetaNueva, bootstyle="primary").grid(row=7, column=4)
        
        # es favorita
        ttk.Label(self.parent, text="Favorita (si o no): ", bootstyle="inverse-dark", padding=3).grid(row=8, column=1)
        checkbutton = ttk.Checkbutton(self.parent,variable=self.fav)
        checkbutton.grid(row=8,column=2)
        

        btn_guardar = ttk.Button(self.parent, text="Guardar", padding=8, bootstyle="success", command=self._rewrite)
        btn_guardar.grid(row=9, column=2)
        texto = '''
DEJAR EN BLANCO LOS CAMPOS QUE NO SE QUIERAN MODIFICAR.
SI QUIERE ELIMINAR UN/A INGREDIENTE/PASO/ETIQUETA, ESCRIBA 'ELIMINAR'
Los ingredientes se deben agregan con un formato como el siguiente ejemplo:
    Ejemplo: Arroz 20 gramos, Sal 1 pizca.
Los pasos se deben agregan separados por coma, como en este ejemplo:
    Ejemplo: Amazar 10 minutos, estirar en una tabla redonda.
Las etiquetas deben estar separadas por coma y un espacio, así:
    Ejemplo: Facil, Rissoto, Arroz.
        '''
        ttk.Label(self.parent, text=texto, bootstyle="inverse-dark", padding=3).grid(row=10, columnspan=3, padx=10)

        # BINDS PARA LOS COMBOBOX
        # self.comboIngredientes.bind("<<ComboboxSelected>>", self.mostrarIngrediente)
        # self.comboPasos.bind("<<ComboboxSelected>>", self.mostrarPaso)
        # self.comboEtiquetas.bind("<<ComboboxSelected>>", self.mostrarEtiqueta)

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)

    def _rewrite(self):
        """funcion para modificar una receta en un archivo json
        Se leerá, y se hará un append a esa lista obtenida al leer"""
        # EN self.receta ES DONDE GUARDAREMOS NUESTRA NUEVA INFORMACION.
        #Como todos los campos van a estar rellenos, directamente guardaremos la info
        data = self._read() #data del archivo.
        
        try:
            recetaNueva = {'nombre': self.nombre.get(),
                        'ingredientes': self._formatearIngredientes(),
                        'preparacion': self._formatearPasos(),
                        'imagen': self.receta['imagen'],
                        'tiempo_preparacion': int(self.preparacion.get()),
                        'tiempo_coccion': int(self.coccion.get()),
                        'fecha_creacion': self.receta['fecha_creacion'],
                        'etiquetas': self._formatearEtiquetas(),
                        'favorita':self.fav.get()
                        }
            
            # se reemplaza el valor de la receta anterior con la nueva info
            index = data.index(self.receta)
            # print(index)
            data[index] = recetaNueva
            # print(recetaNueva)
            try: 
                with open(self.ruta, 'w') as archivo:
                    json.dump(data, archivo)
                
                messagebox.showinfo(message="Todos los datos estan correctos, se guardó la nueva receta.")
                self.parent.destroy()
            except:
                messagebox.showerror(message="Ha habido un error en el guardado.")
        except:
            messagebox.showerror(message="Ha habido un error en algun campo. Por favor revise")
    

    def _formatearPasos(self): #listo
        """se realiza una modificacion en la lista de pasos para retornar la misma con el nuevo valor."""
        # self.listaPasos[self.comboPasos.current()] -> paso anterior
        # self.pasoNuevo.get() -> paso modificado a guardar.
        if self.pasoNuevo.get() != '':
            self.listaPasos[self.comboPasos.current()] = self.pasoNuevo.get()
        #LA PRIMERA POSICION NO ME INTERESA, YA QUE CONTIENE EL VALOR 'Seleccione un paso'
        lista = []
        for paso in self.listaPasos:
            if paso != 'Seleccione un paso' and paso.lower() != 'eliminar':
                lista.append(paso.capitalize())
        
        return lista
        
    def _formatearIngredientes(self): #listo
        """se realizan dos split para obtener una lista de ingredientes (diccionarios) correctamente."""
        # print(self.listaIngredientes[2])
        # print(self.listaIngredientes[2].replace(':', '').split(" "))
        #esta variable, va a ser una lista que contiene diccionarios con tres claves de los ingredientes.
        if self.ingredienteNuevo.get() != '':
            
            ingredienteActualizado= self.ingredienteNuevo.get()
            self.listaIngredientes[self.comboIngredientes.current()] = ingredienteActualizado
            
        lista = []
        for ingrediente in self.listaIngredientes:
            
            if ingrediente != 'Seleccione un Ingrediente' and ingrediente.lower() != 'eliminar':
                datos = ingrediente.replace(':', '').split(" ")
                #datos contiene: en posicion 0 el nombre, en posicion 1 la cantidad y en posicion 2 la unidad, de un ingrediente
                dicc = {'nombre': datos[0].capitalize(), 'cantidad':datos[1], 'unidad':datos[2].capitalize()}
                lista.append(dicc)
        
        return lista

    def _formatearEtiquetas(self): #listo
        """funcion que retorna una lista compuesta por strings."""
        if self.etiquetaNueva.get() != '':
            self.listaEtiquetas[self.comboEtiquetas.current()] = self.etiquetaNueva.get()
            
        lista = []
        for etiqueta in self.listaEtiquetas:
            if etiqueta != 'Seleccione una etiqueta' and etiqueta.lower() != 'eliminar':
                lista.append(etiqueta.capitalize())
        
        return lista
