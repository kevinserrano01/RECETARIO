from tkinter import ttk
import tkinter as tk
import random as r
import json
#para crear una visualizacion de una receta especifica.
from visualizar_RecetaDelDia import VentanaPrincipal as recetaDelDia


class VentanaPrincipal(ttk.Frame):
    """Clase que simula una ventana principal de la aplicacion"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        parent.title('Menú RECETARIO')
        parent.resizable(False, False)
        self.ruta = "recetas.json"
        
        # MENU
        ttk.Button(self.parent, text="Mostrar recetas", command="").grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Mostrar receta del dia", command=self.recetaDia).grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Agregar Receta", command="").grid(row=2, column=2, columnspan=2, padx=10, pady=10, ipadx=15)
        ttk.Button(self.parent, text="Modificar Receta", command="").grid(row=3, column=2, columnspan=2, padx=10, pady=10, ipadx=10)
        ttk.Button(self.parent, text="Eliminar Receta", command="").grid(row=4, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        bottonExit = ttk.Button(self.parent, text="Cerrar", command="")
        bottonExit.grid(row=10, column=2, ipadx=60)
    
    def _read(self, ruta):
        """Lee el archivo JSON"""
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    
    def recetaDia(self):
        recetas = self._read(self.ruta)
        # index = r.randint(0, len(recetas))
        toplevel = tk.Toplevel(self.parent)
        recetaDelDia(toplevel, recetas[1])

root = tk.Tk()
VentanaPrincipal(root).grid()
root.mainloop()