import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from modificar_recetaEntry import App as Secundaria

class Principal(ttk.Frame):
    """Ventana de visualizacion para la modificacion de una receta especifica."""
    def __init__(self, parent, ruta):
        super().__init__(parent)
        self.parent = parent  # Ventana principal
        self.ruta = ruta
        self.RecetaAModificar = tk.StringVar()
        self.campoAModificar = tk.StringVar()
        parent.title("Modificar Receta")
        parent.resizable(False, False)
        ttk.Label(self.parent, text="¿Qué receta deseas modificar?").grid()
        
        ttk.Label(self.parent, text="Ingrese el nombre de la receta a modificar: ").grid(row=1, column=0,padx= 10, pady=20)
        listaNombresReceta = ['Seleccionar opción']
        data = self._read()
        for receta in data:
            listaNombresReceta.append(receta['nombre'])
        
        self.combo = ttk.Combobox(self.parent, textvariable=self.campoAModificar, values=listaNombresReceta)
        self.combo.grid(row=1, column=2, padx=10, pady=20)
        self.combo.current(0)
        
        ttk.Button(self.parent, text="Modificar", bootstyle="info", command=self._modificar).grid(row=3, column=1, columnspan=2)

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)

    def _modificar(self):
        """funcion para modificar una receta en un archivo json
        Se leerá, y se modificara esa receta de la lista obtenida al leer"""
        data = self._read() #data del archivo.

        # ================================================================================================================
        # Aqui se deberia Abrir otra ventana y modificar la receta dato por dato =========================================
        # ================================================================================================================
        if self.campoAModificar.get() != 'Seleccionar opción':
            
           
                #llamada a nueva clase para nueva ventana. 
                toplevel = tk.Toplevel(self.parent)
                Secundaria(toplevel, self.ruta, self.campoAModificar.get()).grid()
                
                
                # self.parent.destroy()
            
        else:
            messagebox.showerror(message=f"Debe seleccionar una opcion correcta :)")
            