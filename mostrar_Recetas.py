from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime
import json

class VentanaPrincipal(ttk.Frame):
    """Clase que muestra TODAS las recetas"""

    def __init__(self, parent, recetas):
        super().__init__()
        self.parent = parent
        parent.title('RECETAS')
        parent.geometry('200x100')
        self.mostrar_recetasTodas(recetas)

    def mostrar_recetasTodas(self, recetas):
        """funcion que muestra todos los nombres de las recetas"""
        for receta in recetas:
            texto =f"Receta: {receta['nombre']}"
            tk.Label(self.parent, text = texto).grid()