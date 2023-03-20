import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from mostrar_Recetas import VentanaPrincipal as mostrarRecetas

class Principal(ttk.Frame):
    """Ventana de visualizacion para la modificacion de una receta especifica."""
    def __init__(self, parent, ruta):
        super().__init__(parent)
        self.parent = parent  # Ventana principal
        self.ruta = ruta
        parent.title("FILTRAR RECETAS")
        parent.resizable(False, False)
        parent.configure(bg='black')
        
        ttk.Label(self.parent, text="Buscar recetas por: ", bootstyle="inverse-dark").grid(row=1, column=0,padx= 10, pady=15)
        ttk.Label(self.parent, text="Filtrar recetas por: ", bootstyle="inverse-dark").grid(row=2, column=0,padx= 10, pady=15)
        
        self.filtro = tk.StringVar()
        opciones =['Seleccione una opcion', 'Nombre de receta', 'Etiquetas de receta']
        
        self.combo = ttk.Combobox(self.parent, textvariable=self.filtro, values=opciones, state="readonly")
        self.combo.grid(row=1, column=2, padx=10, pady=15)
        self.combo.current(0)
        
        self.busqueda = tk.StringVar()
        ttk.Entry(self.parent, textvariable=self.busqueda, bootstyle="primary").grid(row=2, column=2, padx=5, pady=15)
        
        ttk.Button(self.parent, text="FILTRAR", bootstyle="info", command=self.filtrar).grid(row=3, column=1, columnspan=2, pady=10)

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)
        
    def filtrar(self):
        if self.filtro.get() != 'Seleccione una opcion' and self.busqueda.get() != '':
            toplevel = tk.Toplevel(self.parent)
            mostrarRecetas(toplevel, self.ruta, self.filtro.get(), self.busqueda.get())
        else:
            messagebox.showerror(title="ERROR", message="Seleccione una opcion e ingrese un valor.")
