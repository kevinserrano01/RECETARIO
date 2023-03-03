# RECETARIO-with-Python-Tkinter
> Proyecto basado en python junto a una interfaz gráfica con la libreria TKinter para la Universidad Provincial de Administración, Tecnología y Oficios. (UPATecO)

## Recetario de cocina
Para este proyecto se deberá diseñar una aplicación de escritorio en la que puedan crear, editar y eliminar recetas.

> Todos los incisos que tienen el símbolo '✔' son obligatorios, mientras que aquellos que tienen el símbolo '⭐' son opcionales.

Una receta debe estar compuesta de los siguientes datos:

    - Nombre. ✔
    - Una lista de los ingredientes. ✔
    - Preparación, lista ordenada de pasos a seguir. ✔
    - Imagen/es del plato preparado. Una receta puede o no tener una imagen. ✔
    - Tiempo de preparación (en minutos). ✔
    - Tiempo de cocción (en minutos). ✔
    - Fecha de creación. La fecha y hora en que se creó la receta en la aplicación. ✔
    - Etiquetas: palabras clave. ⭐
    - Es favorita (o no). ⭐

Un ingrediente debe contar con la siguiente información:

    - Nombre. ✔
    - Unidad de medida. ✔
    - Cantidad. ✔

Las funcionalidades que debe tener la aplicación son las siguientes:

    - Crear una receta. ✔
    - Modificar una receta. ✔
    - Eliminar una receta. ✔
    - Mostrar “receta del día” aleatoria en la ventana principal. ⭐
    - Buscar y/o filtrar recetas:
        ¬ Nombre. ⭐
        ¬ Por etiquetas. ⭐
        ¬ Tiempo de preparación. ⭐
        ¬ Ingredientes. ⭐

Deberá contar con las siguientes vistas:

- Recetario. Ventana principal por defecto.
- Se muestra un listado de todas las recetas. ✔
- Se mostrará como primera receta de lista a la “receta del día”, la cual debe tener un formato distinto a las demás recetas. ⭐
- Muestra una receta ya existente. ✔
- Carga/modificación de una receta. ✔
- Búsqueda y filtro. La ventana deberá tener un campo de búsqueda, por nombre y/o etiqueta. Una vez filtrados las recetas, se las mostrará en una lista.⭐
