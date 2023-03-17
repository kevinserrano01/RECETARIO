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
        self.ruta = ruta
        self.recetaAEliminar  = tk.StringVar()
        parent.title("Eliminar Receta")
        parent.resizable(False, False)
        
        #BUSCAR LOS NOMBRES DE LAS RECETAS Y GUARDARLOS EN UNA LISTA
        listaRecetas = self.obtenerLista()
        
        ttk.Label(self.parent, text="¿Qué receta deseas eliminar?").grid()
                
        ttk.Label(self.parent, text="Ingrese el nombre de la receta a eliminar: ").grid(row=1, column=0,padx= 10, pady=20)
        self.combo = ttk.Combobox(self.parent, textvariable=self.recetaAEliminar, values=listaRecetas, state="readonly")
        self.combo.grid(row=1, column=2, padx=10, pady=20)
        self.combo.current(0)
        self.combo.focus()
        
        # ttk.Entry(self.parent, textvariable=self.recetaAEliminar ).grid(row=1, column=2, padx=10, pady=20)
        
        ttk.Button(self.parent, text="Eliminar", bootstyle="info", command=self._eliminar).grid(row=2, column=1, columnspan=2)

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
            
        # print(data.index(self.recetaAEliminar.get()))
        # data.pop(self.recetaAEliminar)
        
    # def _eliminar(self):
    #     """funcion para eliminar una receta en un archivo json
    #     Se leerá, y se eliminará esa receta de la lista obtenida al leer"""
    #     data = self._read() #data del archivo.
        
    #     buscado = self._buscarReceta()
    #     if buscado != int(-1):#La receta existe, entonces se elimina.
    #         #se ejecuta la eliminacion a traves del metodo pop(indice)
    #         recetaEliminada = data.pop(buscado)
    #         try:
    #             #se escribe de nuevo el archivo.
    #             self._write(data)
    #             messagebox.showinfo(message=f"Se encontró y se elimino la receta '{recetaEliminada['nombre']}'")
    #             self.parent.destroy()
    #         except:
    #             messagebox.showerror(message=f"Hubo un error al eliminar la receta.\nIntente nuevamente.")
    #             self.parent.destroy()
    #     else:#no esta la receta en la lista.
    #         messagebox.showinfo(message=f"No se encontro la receta '{self.recetaAEliminar.get()}'")
            
    # def _buscarReceta(self):
    #     """Funcion para buscar si una receta existe en un archivo JSON.
    #     retorna -1 si no encuentra, o la posicion del elemento buscado"""
    #     data = self._read() #data del archivo.
    #     i = -1 #variable de control
    #     for receta in data:
    #         # Para que la comparacion sea correcta, llevamos todo a minuscula para compararlo
    #         if (self.recetaAEliminar.get()).lower() == (receta['nombre']).lower():
    #         #solo si está en la lista, se ejecuta lo siguiente 
    #         #(porque .index tira error si no esta el elemento en la lista)
    #             i = data.index(receta)
                
    #     # en caso de que no esté, se retorna -1
    #     return i