from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from visualizar_RecetaDelDia import VentanaPrincipal as verReceta

class VentanaPrincipal(ttk.Frame):
    """Clase que muestra TODAS las recetas en base a lo filtrado (nombre o etiqueta) y la busqueda (lo que ingresa el usuario)"""

    def __init__(self, parent, ruta, filtrado, busqueda):
        super().__init__()
        self.parent = parent
        parent.geometry("150x250")
        parent.configure(bg='black')
        self.ruta = ruta
        self.filtrado = filtrado
        self.busqueda = busqueda
        parent.title('RESULTADOS DE RECETAS FILTRADAS')
        parent.resizable(False, False)

        parent.configure(bg='black')
        self.recetas = self._read()
        
        self.resultados = self.filtrarRecetas()
        nombres = tk.Variable(value = [receta['nombre'] for receta in self.resultados])
        
        self.listbox = tk.Listbox(self.parent, listvariable=nombres, selectmode=tk.SINGLE, height=len(self.resultados))
        self.listbox.grid(row=0, column=1,columnspan=3, padx=10, pady=10)
        ttk.Button(self.parent, text="Mostrar receta", bootstyle="info-outline",command=self.mostrarRecetaIndividual).grid(row=2, column=1, padx=10, pady=10, columnspan=3)
        
    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)
        
    def filtrarRecetas(self):
        """funcion que filtra recetas por nombre y etiqueta que devuelve una lista con sus resultados."""
        listaResultados = []
        
        for receta in self.recetas:
                #si entra aca, es porque el filtrado es = Nombre de receta
            if  self.filtrado == 'Nombre de receta':
                if self.busqueda.lower() in receta['nombre'].lower():
                    listaResultados.append(receta)
            else:
                #si entra aca, es porque el filtrado es = Etiquetas de receta
                for etiqueta in receta['etiquetas']:
                    if self.busqueda.lower() in etiqueta.lower(): 
                        listaResultados.append(receta)
                        break 
                    
        return listaResultados
      
    def mostrarRecetaIndividual(self):
        """Funcion que muestra una receta deseada por el usuario"""
        seleccion = self.listbox.curselection()
        if seleccion:
            nombreReceta = self.listbox.get(seleccion)
            for receta in self.resultados:
                if receta['nombre'].lower() == nombreReceta.lower():
                    toplevel = tk.Toplevel(self.parent)
                    verReceta(toplevel, receta)
        else:
            messagebox.showinfo(message=f"Debe seleccionar un item de la lista.")