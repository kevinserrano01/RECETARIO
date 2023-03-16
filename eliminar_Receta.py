import tkinter as tk
from tkinter import ttk, messagebox
import json

class Principal(ttk.Frame):
    def __init__(self, parent, ruta):
        super().__init__(parent)
        self.parent = parent # Ventana principal
        self.ruta= ruta
        parent.title("Eliminar Receta")