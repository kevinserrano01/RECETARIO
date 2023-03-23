import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json


class Principal(ttk.Frame):
    """Ventana de visualizacion para eliminacion de una receta especifica."""
    def __init__(self, parent, ruta):
        super().__init__(parent)
        self.parent = parent  # Ventana principal
        parent.configure(bg='black')
        self.ruta = ruta
        self.recetaAEliminar  = tk.StringVar()
        parent.title("Eliminar Receta")
        parent.resizable(False, False)
        
        #BUSCAR LOS NOMBRES DE LAS RECETAS Y GUARDARLOS EN UNA LISTA
        listaRecetas = self.obtenerLista()
        
        ttk.Label(self.parent, text="¿Qué receta deseas eliminar?", bootstyle="inverse-dark").grid()
                
        ttk.Label(self.parent, text="Ingrese el nombre de la receta a eliminar: ", bootstyle="inverse-dark").grid(row=1, column=0,padx= 10, pady=20)
        self.combo = ttk.Combobox(self.parent, textvariable=self.recetaAEliminar, values=listaRecetas, state="readonly")
        self.combo.grid(row=1, column=2, padx=10, pady=20)
        self.combo.current(0)
        self.combo.focus()
                
        ttk.Button(self.parent, text="Eliminar", bootstyle="danger", command=self._eliminar).grid(row=2, column=1, columnspan=2, pady=10)

    def _read(self):
        """Lee el archivo JSON"""
        with open(self.ruta, 'r') as archivo:
            return json.load(archivo)

    def _write(self, data):
        """Escribe un archivo JSON"""
        with open(self.ruta, 'w') as archivo:
            json.dump(data, archivo)
    
    def obtenerLista(self):
        """funcion que retorna una lista de los nombres de las recetas del archivo JSON"""
        lista = ['Seleccione una receta']
        data = self._read()
        for receta in data:
            lista.append(receta['nombre'])
        return lista  
        
    def _eliminar(self):
        """Funcion para eliminar una receta del archivo JSON"""
        data = self._read()
        if self.recetaAEliminar.get() != 'Seleccione una receta':
            for receta in data:
                if receta['nombre'] == self.recetaAEliminar.get():
                    index = data.index(receta)
            
            data.pop(index)
            #ya se borro la receta, asi que se escribe de nuevo el archivo con el resto de recetas.
            self._write(data)
            messagebox.showinfo(title="EXITO", message="Se ha borrado la receta correctamente :D")
            self.parent.destroy()
        else:
            messagebox.showwarning(title="RECOMENDACION", message="Seleccione una receta. :D")