from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import datetime
import json

class VentanaPrincipal(ttk.Frame):
    """Clase que muestra una receta especifica (RECETA DEL DIA)

    Args:
        ttk (_type_): _description_
    """
    def __init__(self, parent, receta):
        super().__init__()
        self.parent = parent
        parent.title('RECETA DEL DIA')
        parent.geometry('400x500')
        nombre = receta['nombre']
        title = f'{nombre} '
        label = tk.Label(self.parent, text=title, justify='left', font='bold')
        label.pack()
        # imagen
        self.canvas = Canvas(self.parent, width=300, height=300)
        self.canvas.pack()
        imagen = Image.open(receta['imagen'])
        imagen = imagen.resize((300, 250))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.canvas.create_image(0, 0, anchor=NW, image=self.imagen_tk)
        # buttons que abren otra ventana
        self.ingredientes = receta['ingredientes']
        btnIngreditnes = tk.Button(self.parent, text="Ingredientes", command=self.abrir_ventanaIng)
        btnIngreditnes.pack()
        self.pasos = receta['preparacion']
        btnPreparacion = tk.Button(self.parent, text="Pasos Preparacion",command=self.abrir_ventanaPasos)
        btnPreparacion.pack()
        # tiempo de coccion
        time_coccion = receta['tiempo_coccion']
        label = tk.Label(self.parent, text=f"Tiempo de coccion: {time_coccion}", justify='left')
        label.pack()
        # fecha de creacion
        fecha = receta['fecha_creacion']
        fecha_creacion = f'Fecha de creacion: {fecha}'
        label = tk.Label(self.parent, text=fecha_creacion, justify='left')
        label.pack()
        # tiempo de preparacion
        preparacion = receta['tiempo_preparacion']
        time_coccion = f'Tiempo de preparacion: {preparacion}'
        label = tk.Label(self.parent, text=time_coccion, justify='left')
        label.pack()
        # es favorita
        favorita = receta['favorita']
        label = tk.Label(self.parent, text=f"Es favorita: {'Sí' if favorita else 'No'}", justify='left')
        label.pack()
        
    def abrir_ventanaIng(self):
        """Abre una ventada para visualizar los ingredientes de cada receta"""
        if len(self.ingredientes) > 0:
            toplevel = Toplevel(self.parent)
            SecundariaIngredientes(toplevel, self.ingredientes).grid()
        else:
            messagebox.showwarning(message="No tiene ingredientes, no se puede preparar :c")
            
    def abrir_ventanaPasos(self):
        """Abre una ventada para visualizar los pasos de cada receta"""
        if len(self.pasos) > 0:
            toplevel = Toplevel(self.parent)
            SecundariaPasos(toplevel, self.pasos).grid()
        else:
            messagebox.showwarning(message="No tiene pasos, no se puede preparar :c")
        
class SecundariaIngredientes(ttk.Frame):
    """ABRE UNA VENTANA SECUNDARIA PARA LA VISUALIZACION DE INGREDIENTES DE UNA RECETA.

    Args:
        ttk (_type_): _description_
    """
    def __init__(self, parent, ingredientes):
        super().__init__(parent, padding=(20))
        self.parent = parent
        parent.title("Ingredientes")
        parent.geometry("350x100+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        self.mostrar_Ingredientes(ingredientes)
        
    def mostrar_Ingredientes(self, ingredientes):
        """funcion que muestra los ingredientes en la ventana"""
        for ingrediente in ingredientes:
            texto =f"{ingrediente['nombre']}: {ingrediente['cantidad']} {ingrediente['unidad']}"
            tk.Label(self.parent, text = texto).grid()

class SecundariaPasos(ttk.Frame):
    """ABRE UNA VENTANA SECUNDARIA PARA LA VISUALIZACION DE LOS PASOS DE UNA RECETA.

    Args:
        ttk (_type_): _description_
    """
    def __init__(self, parent, pasos):
        super().__init__(parent, padding=(20))
        self.parent = parent
        parent.title("Pasos de Preparacion")
        parent.geometry("+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        self.mostrar_pasos(pasos)
        
    def mostrar_pasos(self, pasos):
        """Printea los pasos en la ventana."""
        # tabla = ttk.Treeview(self.parent, columns=("#1")).grid()
        # tabla.column("#0", width=80, anchor=CENTER)
        # tabla.column("#1", width=80, anchor=CENTER)
        
        # tabla.heading("#0", text ="Indice", anchor=CENTER)
        # tabla.heading("#1", text ="Descripcion", anchor=CENTER)
        i = 1
        for paso in pasos:
            texto = f"paso {i} - {paso.capitalize()}"
            i += 1
            tk.Label(self.parent, text = texto).grid()

    