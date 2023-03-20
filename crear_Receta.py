import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from datetime import datetime 

class App(ttk.Frame):
    def __init__(self, parent, ruta):
        super().__init__(parent, padding=(10))
        self.parent = parent # referencia a la ventana ppal
        parent.title("Crear receta")
        self.ruta= ruta
        parent.configure(bg='black')
        # variables de datos a guardar
        self.nombre = tk.StringVar()
        self.ingredientes = tk.StringVar()
        self.pasos = tk.StringVar()
        self.imagen = tk.StringVar()
        self.preparacion = tk.StringVar()
        self.coccion = tk.StringVar()
        self.etiquetas = tk.StringVar()
        self.fav = tk.BooleanVar()
        # labels y entryes para cada campo a agregar.
        
        ttk.Label(self.parent, text="Nombre: *", padding=3, bootstyle="inverse-dark").grid(row=1, column=1, padx=10, pady=5)
        ttk.Entry(self.parent, textvariable=self.nombre, bootstyle="primary").grid(row=1, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Ingredientes: *", padding=3, bootstyle="inverse-dark").grid(row=2, column=1, padx=10, pady=5)
        ttk.Entry(self.parent, textvariable=self.ingredientes, bootstyle="primary").grid(row=2, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Pasos para la preparacion: *", padding=3, bootstyle="inverse-dark").grid(row=3, column=1, padx=10, pady=5)
        ttk.Entry(self.parent,textvariable=self.pasos, bootstyle="primary").grid(row=3, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Imagen: ", padding=3, bootstyle="inverse-dark").grid(row=4, column=1, padx=10, pady=5)
        ttk.Entry(self.parent,textvariable=self.imagen, bootstyle="primary").grid(row=4, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Tiempo preparacion (min): *", padding=3, bootstyle="inverse-dark").grid(row=5, column=1, padx=10, pady=5)
        ttk.Entry(self.parent,textvariable=self.preparacion, bootstyle="primary").grid(row=5, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Tiempo de coccion (min): *", padding=3, bootstyle="inverse-dark").grid(row=6, column=1, padx=10, pady=5)
        ttk.Entry(self.parent,textvariable=self.coccion, bootstyle="primary").grid(row=6, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Etiquetas: *", padding=3, bootstyle="inverse-dark").grid(row=7, column=1, padx=10, pady=5)
        ttk.Entry(self.parent,textvariable=self.etiquetas, bootstyle="primary").grid(row=7, column=2, padx=10, pady=5)
        
        ttk.Label(self.parent, text="Favorita (si o no): ", padding=3, bootstyle="inverse-dark").grid(row=8, column=1, padx=10, pady=5)
        ttk.Checkbutton(self.parent,variable=self.fav, bootstyle="success-round-toggle").grid(row=8,column=2, padx=10, pady=5)

        btn_guardar = ttk.Button(self.parent, bootstyle="success", text="Guardar", padding=8, command=self._write)
        btn_guardar.grid(row=9, column=2, padx=5, pady=5)
        texto = '''
Los campos con * son obligatorios
Los ingredientes se deben agregan con un formato como el siguiente ejemplo:
    Ejemplo: Arroz 20 gramos, Sal 1 pizca.
Los pasos se deben agregan separados por coma, como en este ejemplo:
    Ejemplo: Amazar 10 minutos, estirar en una tabla redonda.
Las etiquetas deben estar separadas por coma y un espacio, así:
    Ejemplo: Facil, Rissoto, Arroz.
        '''
        ttk.Label(self.parent, text=texto, padding=3, bootstyle="inverse-dark").grid(row=10, columnspan=3, padx=10, pady=10)


    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)

    def _write(self):
        """funcion para cargar una receta en un archivo json
        Se leerá, y se hará un append a esa lista obtenida al leer"""
        data = self._read() #data del archivo.
        if self.validacionCampos():
            #campos correctos, entonces se agrega.
            try:
                fecha_creacion = f"{datetime.now().year}/{datetime.now().month}/{datetime.now().day}"
                
                recetaNueva = {'nombre': self.nombre.get(),
                            'ingredientes': self._formatearIngredientes(),
                            'preparacion': self._formatearPasos(),
                            'imagen': self.imagen.get(),
                            'tiempo_preparacion': int(self.preparacion.get()),
                            'tiempo_coccion': int(self.coccion.get()),
                            'fecha_creacion': fecha_creacion,
                            'etiquetas': self.etiquetas.get().split(', '),
                            'favorita':self.fav.get()
                            }
                
                # se agrega el archivo al json
                data.append(recetaNueva)
                try: 
                    with open(self.ruta, 'w') as archivo:
                        json.dump(data, archivo)
                    
                    messagebox.showinfo(message="Todos los datos estan correctos, se guardó la nueva receta.")
                except:
                    messagebox.showerror(message="Ha habido un error en el guardado.")
                    
            except:
                messagebox.showerror(message="Ha habido un error. Por favor, vuelva a intentar")
        self.parent.destroy()
            
    def validacionCampos(self):
        if self.nombre.get() == "":
            messagebox.showerror(message="El campo nombre está vacio")
            return False
        elif self.pasos.get() == "":
            messagebox.showerror(message="El campo pasos está vacio")
            return False
        elif self.ingredientes.get() == "":
            messagebox.showerror(message="El campo ingredientes está vacio")
            return False
        elif self.preparacion.get() == "":
            messagebox.showerror(message="El campo preparacion está vacio")
            return False
        elif self.coccion.get() == "":
            messagebox.showerror(message="El campo coccion está vacio")
            return False
        else:
            return True
    
    def _formatearPasos(self):
        """se realiza un split para obtener una lista de pasos formateado correctamente"""
        return self.pasos.get().split(", ")
        
    def _formatearIngredientes(self):
        """se realizan dos split para obtener una lista de ingredientes correctamente."""
        # esta variable, va a ser una lista que contiene diccionarios con tres claves de los ingredientes.
        ListaDeIngredientes = []
        lista = self.ingredientes.get().split(", ")
        for ingrediente in lista:
            datos = ingrediente.split(" ")
            #datos contiene: en posicion 0 el nombre, en posicion 1 la cantidad y en posicion 2 la unidad
            dicc = {'nombre': datos[0], 'cantidad':datos[1], 'unidad':datos[2]}
            ListaDeIngredientes.append(dicc)
        
        return ListaDeIngredientes