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
        parent.configure(bg='black')
        self.ruta = ruta
        self.filtrado = filtrado
        self.busqueda = busqueda
        parent.title('RESULTADOS DE RECETAS FILTRADAS')
        parent.resizable(False, False)

        parent.configure(bg='black')
        self.recetas = self._read()
        self.mostrar_recetas()
        

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
        
    def mostrar_recetas(self):
        """funcion que muestra todos los nombres de las recetas"""
        resultados = self.filtrarRecetas()
        
        # print([element['nombre'] for element in resultados])
        
        if len(resultados) == 0:
            messagebox.showinfo(title="RESULTADO DE BUSQUEDA DE RECETAS", message="No se encontraron recetas con la informacion deseada.")
            self.parent.destroy()
        else:
            for indice, receta in enumerate(resultados):
                # PREGUNTAR ACA AL PROFE
                ttk.Label(self.parent, text = f"Receta: {receta['nombre']}", bootstyle="inverse-secondary").grid(row=indice,column=0, padx=10, pady=15)
                ttk.Button(self.parent, bootstyle="success", text='ver receta', command=lambda: self.mostrarRecetaIndividual(receta)).grid(row=indice,column=1, padx=10, pady=5)
                       
            
    def mostrarRecetaIndividual(self, receta):
        """Funcion que muestra una receta deseada por el usuario"""
        
        resultados = self.filtrarRecetas()
        index = resultados.index(receta)
        print(index)
        
        toplevel = tk.Toplevel(self.parent)
        verReceta(toplevel, resultados[index])