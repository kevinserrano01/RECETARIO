from tkinter import ttk
import tkinter as tk
import random as r
import json
#para crear una visualizacion de una receta especifica.
from visualizar_RecetaDelDia import VentanaPrincipal as recetaDelDia
from crear_Receta import App as crearReceta


class VentanaPrincipal(ttk.Frame):
    """Clase que simula una ventana principal de la aplicacion"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        parent.title('Menú RECETARIO')
        parent.resizable(False, False)
        self.ruta = "recetas.json"
        # Poner icono en la ventana principal
        # self.icon = tk.PhotoImage(file=icon)
        # self.set_icon()
        # self.parent.iconphoto(True, self.icon)
        
        
        # MENU
        ttk.Button(self.parent, text="Mostrar recetas", command="").grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Mostrar receta del dia", command=self.recetaDia).grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Agregar Receta", command=self.crear_receta).grid(row=2, column=2, columnspan=2, padx=10, pady=10, ipadx=15)
        ttk.Button(self.parent, text="Modificar Receta", command="").grid(row=3, column=2, columnspan=2, padx=10, pady=10, ipadx=10)
        ttk.Button(self.parent, text="Eliminar Receta", command="").grid(row=4, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        bottonExit = ttk.Button(self.parent, text="Cerrar", command=parent.destroy)
        bottonExit.grid(row=10, column=2, ipadx=60)
    
    # def set_icon(self):
    #     self.parent.iconphoto(True, self.icon)

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)
    
    def recetaDia(self):
        """Funcion para abrir una ventana secundaria donde se mostrará una receta random entre las que esten en el archivo JSON"""
        recetas = self._read()
        index = r.randint(0, len(recetas)-1)
        toplevel = tk.Toplevel(self.parent)
        recetaDelDia(toplevel, recetas[index]).grid()
    
    def crear_receta(self):
        """Funcion para abrir una ventana secundaria donde se mostrará todos los campos para ingresar los datos de una nueva receta"""
        toplevel = tk.Toplevel(self.parent)
        crearReceta(toplevel, self.ruta)

#funcionamiento
root = tk.Tk()
VentanaPrincipal(root).grid()
root.mainloop()
