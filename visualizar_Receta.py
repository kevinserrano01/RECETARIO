from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Receta de muestra')
        self.geometry('400x500')
        title = 'Titulo: Empanadas Arabes'
        label = tk.Label(self, text=title, justify='left', font='bold')
        label.pack()
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.pack()
        imagen = Image.open("images\EmpanadasArabes.jpg")
        imagen = imagen.resize((300, 250))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.canvas.create_image(0, 0, anchor=NW, image=self.imagen_tk)
        # buttons que abren otra ventana
        btnIngreditnes = tk.Button(self, text="Ingredientes", command=self.mostrar_Ingredientes)
        btnIngreditnes.pack()
        btnPreparacion = tk.Button(self, text="Pasos Preparacion", command=self.mostrar_Preparacion)
        btnPreparacion.pack()
        # Textos
        time_coccion = 'Tiempo de coccion: 30 min'
        label = tk.Label(self, text=time_coccion, justify='left')
        label.pack()
        fecha_creacion = 'Fehca de creacion: 08/03/2023'
        label = tk.Label(self, text=fecha_creacion, justify='left')
        label.pack()
        time_coccion = 'Tiempo de coccion: 30 min'
        label = tk.Label(self, text=time_coccion, justify='left')
        label.pack()
        fav = 'Favorita: Si'
        label = tk.Label(self, text=fav, justify='left')
        label.pack()

    def mostrar_Ingredientes(self):
        pass

    def mostrar_Preparacion(self):
        pass

class SegundaVentana(tk.Tk):
    def __init__(self):
        super().__init__()

    def ventada2(self):
        pass


root = VentanaPrincipal()
root.mainloop()