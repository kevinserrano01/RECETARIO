from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from visualizar_RecetaDelDia import VentanaPrincipal as verReceta

class VentanaPrincipal(ttk.Frame):
    """Clase que muestra TODAS las recetas"""

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
        
        self.mostrar_recetasTodas()
        

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)
        
    def mostrar_recetasTodas(self):
        """funcion que muestra todos los nombres de las recetas"""
        i = 0 #variable de control para saber si se printio alguna receta
        for indice , receta in enumerate(self.recetas, 0):
            if  self.filtrado == 'Nombre de receta':
                if self.busqueda.lower() in receta['nombre'].lower():
                    
                    texto =f"Receta: {receta['nombre']}"
                    ttk.Label(self.parent, text = texto, bootstyle="inverse-secondary").grid(row=indice, column = 0, padx=10, pady=15)
                    ttk.Button(self.parent, bootstyle="success", text='ver receta', command=lambda: self.mostrarReceta(receta)).grid(row=indice,column=1, padx=10, pady=3)
                    i+=1
            else:
                #si entra aca, es porque el filtrado es = Etiquetas de receta
                receta['etiquetas'] 
                for etiqueta in receta['etiquetas']:
                        
                    if self.busqueda.lower() in etiqueta.lower():
                        
                        texto =f"Receta: {receta['nombre']}"
                        ttk.Label(self.parent, text = texto, bootstyle="inverse-secondary").grid(row=indice,column=0, padx=10, pady=15)
                        ttk.Button(self.parent, bootstyle="success", text='ver receta', command=lambda: self.mostrarReceta(receta)).grid(row=indice,column=1, padx=10, pady=5)
                        i+=1
                        #cerramos el ciclo interno de etiquetas, si es que al menos una etiqueta tiene lo buscado en self.busqueda
                        break 
        if i== 0:
            messagebox.showinfo(title="RESULTADO DE BUSQUEDA DE RECETAS", message="No se encontraron recetas con la informacion proporcionada.")
            self.parent.destroy()
            
    def mostrarReceta(self, receta):
        toplevel = tk.Toplevel(self.parent)
        verReceta(toplevel, receta)