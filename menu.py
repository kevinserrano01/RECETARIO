import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random as r
import json
#para crear una visualizacion de una receta especifica.
from visualizar_RecetaDelDia import VentanaPrincipal as recetaDelDia
from crear_Receta import App as crearReceta
from eliminar_Receta import Principal as eliminarReceta
from modificar_Receta import Principal as modificarReceta
from filtro_Recetas import Principal as filtrarReceta
# from mostrar_Recetas import VentanaPrincipal as mostrarRecetas

class VentanaPrincipal(ttk.Frame):
    """Clase que simula una ventana principal de la aplicacion"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        parent.title('Menú RECETARIO')
        parent.resizable(False, False)
        parent.configure(bg='black')
        self.ruta = "recetas.json"

        # Poner icono en la ventana principal
        #FORMA 2
        # self.icon = tk.PhotoImage(file='icon-Recetario.jpg')
        # # self.set_icon()
        # self.parent.iconphoto(True, self.icon)
    
        # def set_icon(self):
        #     self.parent.iconphoto(True, self.icon)
    
        #FORMA 1
        # parent.tk.call('wm', 'iconphoto', parent._w, tk.PhotoImage(file='./icon/icon-recetario.ico'))

        # MENU
        ttk.Button(self.parent, text="Filtrar recetas", bootstyle="info-outline", command=self.mostrar_recetas).grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Mostrar receta del dia", bootstyle="info-outline", command=self.recetaDia).grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        ttk.Button(self.parent, text="Agregar Receta", bootstyle="info-outline", command=self.crear_receta).grid(row=2, column=2, columnspan=2, padx=10, pady=10, ipadx=15)
        ttk.Button(self.parent, text="Modificar Receta", bootstyle="info-outline", command=self.modificar_receta).grid(row=3, column=2, columnspan=2, padx=10, pady=10, ipadx=10)
        ttk.Button(self.parent, text="Eliminar Receta", bootstyle="info-outline", command=self.eliminar_receta).grid(row=4, column=2, columnspan=2, padx=10, pady=10, ipadx=14)
        separador = ttk.Separator(bootstyle="info")
        separador.grid(row=10, column=2, ipadx=150)
        bottonExit = ttk.Button(self.parent, text="Cerrar", bootstyle="danger", command=parent.destroy)
        bottonExit.grid(row=11, column=2, ipadx=60, pady=20)

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

    def eliminar_receta(self):
        """Funcion para eliminar una receta deseada por el usuario del archivo JSON"""
        toplevel = tk.Toplevel(self.parent)
        eliminarReceta(toplevel, self.ruta)

    def modificar_receta(self):
        """Funcion para modificar una receta deseada por el usuario del archivo JSON"""
        toplevel = tk.Toplevel(self.parent)
        modificarReceta(toplevel, self.ruta)

    def mostrar_recetas(self):
        """Funcion para mostrar todas las recetas"""
        recetas = self._read()
        toplevel = tk.Toplevel(self.parent)
        filtrarReceta(toplevel, self.ruta)


#funcionamiento
root = tk.Tk()
VentanaPrincipal(root).grid()
root.mainloop()
