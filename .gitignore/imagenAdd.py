import cv2
from tkinter import *

# Leer la imagen utilizando OpenCV
img = cv2.imread('Recetario-Project\images\pastelDeChocolate.jpg')

# Convertir la imagen a un formato compatible con Tkinter
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Crear una ventana en Tkinter
root = Tk()

# Crear una etiqueta en Tkinter
label = Label(root)

# Colocar la imagen en la etiqueta
label.img = PhotoImage(data=img.tostring())
label.config(image=label.img)

# Mostrar la etiqueta en la ventana
label.pack()

# Ejecutar el bucle principal de Tkinter
root.mainloop()
