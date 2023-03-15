import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent # referencia a la ventana ppal
        parent.title("Crear receta")
        self.nombre = tk.StringVar()
        self.ingredientes = tk.StringVar()
        self.pasos = tk.StringVar()
        self.imagen = tk.StringVar()
        self.preparacion = tk.StringVar()
        self.coccion = tk.StringVar()
        self.fecha = tk.StringVar()
        ttk.Label(self, text="Nombre", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.nombre).grid(row=1, column=2)
        ttk.Label(self, text="Ingredientes", padding=3).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.ingredientes).grid(row=2, column=2)
        ttk.Label(self, text="Pasos para la preparacion", padding=3).grid(row=3, column=1)
        ttk.Entry(self,textvariable=self.pasos).grid(row=3, column=2)
        ttk.Label(self, text="Imagen", padding=3).grid(row=4, column=1)
        ttk.Entry(self,textvariable=self.imagen).grid(row=4, column=2)
        ttk.Label(self, text="Tiempo preparacion (min):", padding=3).grid(row=5, column=1)
        ttk.Entry(self,textvariable=self.preparacion).grid(row=5, column=2)
        ttk.Label(self, text="Tiempo de coccion: ", padding=3).grid(row=6, column=1)
        ttk.Entry(self,textvariable=self.coccion).grid(row=6, column=2)
        ttk.Label(self, text="Fecha de creacion", padding=3).grid(row=7, column=1)
        ttk.Entry(self,textvariable=self.fecha).grid(row=7, column=2)
        btn_guardar = ttk.Button(self, text="Guardar", padding=3, command=self.guardar)
        btn_guardar.grid(row=8, column=2)
        
        parent.bind('<Return>', lambda e: btn_guardar.invoke()) 

    def guardar(self):
        print(f"Datos guardados: {self.nombre.get()}, {self.ingredientes.get()}, {self.pasos.get()}, {self.imagen.get()}, {self.preparacion.get()}, {self.coccion.get()}, {self.fecha.get()}")
        self.parent.destroy() # terminamos el programa al destruir la ventana principal
    
root = tk.Tk()
App(root).grid()
# root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
root.mainloop()



#Sabemos que funciona, pero es dinamico

# class App(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent, padding=(10))
#         self.parent = parent # referencia a la ventana ppal
#         parent.title("Crear receta")
#         self.nombre = tk.StringVar()
#         self.ingredientes = tk.StringVar()
#         self.pasos = tk.StringVar()
#         self.imagen = tk.StringVar()
#         self.preparacion = tk.StringVar()
#         self.coccion = tk.StringVar()
#         self.fecha = tk.StringVar()
#         ttk.Label(self, text="Nombre", padding=3).grid(row=1, column=1)
#         ttk.Entry(self, textvariable=self.nombre).grid(row=1, column=2)
#         ttk.Label(self, text="Ingredientes", padding=3).grid(row=2, column=1)
#         ttk.Entry(self, textvariable=self.ingredientes).grid(row=2, column=2)
#         ttk.Label(self, text="Pasos para la preparacion", padding=3).grid(row=3, column=1)
#         ttk.Entry(self,textvariable=self.pasos).grid(row=3, column=2)
#         ttk.Label(self, text="Imagen", padding=3).grid(row=4, column=1)
#         ttk.Entry(self,textvariable=self.imagen).grid(row=4, column=2)
#         ttk.Label(self, text="Tiempo preparacion (min):", padding=3).grid(row=5, column=1)
#         ttk.Entry(self,textvariable=self.preparacion).grid(row=5, column=2)
#         ttk.Label(self, text="Tiempo de coccion: ", padding=3).grid(row=6, column=1)
#         ttk.Entry(self,textvariable=self.coccion).grid(row=6, column=2)
#         ttk.Label(self, text="Fecha de creacion", padding=3).grid(row=7, column=1)
#         ttk.Entry(self,textvariable=self.fecha).grid(row=7, column=2)
#         btn_guardar = ttk.Button(self, text="Guardar", padding=3, command=self.guardar)
#         btn_guardar.grid(row=8, column=2)
        
#         parent.bind('<Return>', lambda e: btn_guardar.invoke()) 

#     def guardar(self):
#         print(f"Datos guardados: {self.nombre.get()}, {self.ingredientes.get()}, {self.pasos.get()}, {self.imagen.get()}, {self.preparacion.get()}, {self.coccion.get()}, {self.fecha.get()}")
#         self.parent.destroy() # terminamos el programa al destruir la ventana principal
    
# root = tk.Tk()
# App(root).grid()
# # root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
# root.mainloop()