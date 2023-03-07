# desarrollar clase de Receta y clase Ingrediente.
# una receta va a recibir sus datos, entre ellos, ingredientes.

# ver si la lista de ingredientes puede llegar a ser una lista de diccionarios
# donde cada diccionario sea el ingrediente, es decir, contenga su nombre, unidad de medida y cantidad.
class Ingrediente:
    """CLASE QUE REPRESENTA UN INGREDIENTE DE UNA RECETA"""

    def __init__(self, nombre, unidad_Medida, cant):
        """CONSTRUCTOR DE CLASE QUE RECIBE NOMBRE, UNIDAD DE MEDIDA Y CANTIDAD DEL INGREDIENTE"""
        self.nombre = nombre
        self.unidadMedida = unidad_Medida
        self.cantidad = cant

    def __str__(self):
        """METODO QUE MUESTRA UN INGREDIENTE."""
        print(f"{self.nombre}: {self.cantidad} {self.unidadMedida}")


class Receta:
    """CLASE QUE REPRESENTA UNA RECETA"""

    recetas = []

    def __init__(self, nombre, Listingredientes):
        """CONSTRUCTOR DE CLASE QUE RECIBE NOMBRE(str), INGREDIENTES(dicc del tipo Ingrediente), LISTA DE PASOS(str), IMAGEN DE PLATO
        TIEMPO DE PREPARACION(min), TIEMPO DE COCCION(min), ETIQUETAS (lista de palabras), FAVORITA (boolean)"""
        self.nombre = nombre
        self.ingredientes = []
        # recorrer cada dicc en la lista y transformarlo en una instancia de clase Ingrediente
        for ingred in Listingredientes:
            ingrediente = Ingrediente(
                ingred['nombre'], ingred['UnidadMedida'], ingred['cantidad'])
            self.ingredientes.append(ingrediente)

    def mostrar_ingredientes(self):
        """FUNCION PARA MOSTRAR LOS INGREDIENTES DE LA RECETA (provisorio creo)"""
        print(f"INGREDIENTES PARA PREPARAR: *{self.nombre}*")
        for ingrediente in self.ingredientes:
            ingrediente.__str__()


Recetas = []

ingredientes = [{'nombre': 'arroz', 'cantidad': 150, 'UnidadMedida': 'gr'}, {'nombre': 'Calabaza', 'cantidad': 200, 'UnidadMedida': 'gr'}, {'nombre': 'cebolla', 'cantidad': 1, 'UnidadMedida': 'unidad'},
                {'nombre': 'Caldo', 'cantidad': 0.5, 'UnidadMedida': 'litros'}, {'nombre': 'vino blanco', 'cantidad': 1,'UnidadMedida': 'vaso'}, {'nombre': 'manteca', 'cantidad': 1, 'UnidadMedida': 'cucharita'},
                {'nombre': 'Queso parmesano', 'cantidad': 30, 'UnidadMedida': 'gr'}, {'nombre': 'Sal', 'cantidad': 1, 'UnidadMedida': 'cucharita'}, {'nombre': 'Pimienta', 'cantidad': 1, 'UnidadMedida': 'cucharita'}]

ingredientes2 = [{'nombre': 'carnee', 'cantidad': 150, 'UnidadMedida': 'gr'}, {'nombre': 'Calabaza', 'cantidad': 200, 'UnidadMedida': 'gr'}, {'nombre': 'cebolla', 'cantidad': 1, 'UnidadMedida': 'unidad'},
                {'nombre': 'Caldo', 'cantidad': 0.5, 'UnidadMedida': 'litros'}, {'nombre': 'vino blanco', 'cantidad': 1,'UnidadMedida': 'vaso'}, {'nombre': 'manteca', 'cantidad': 1, 'UnidadMedida': 'cucharita'},
                {'nombre': 'Queso parmesano', 'cantidad': 30, 'UnidadMedida': 'gr'}, {'nombre': 'Sal', 'cantidad': 1, 'UnidadMedida': 'cucharita'}, {'nombre': 'Pimienta', 'cantidad': 1, 'UnidadMedida': 'cucharita'}]

Nombre_Receta = 'Risotto de Calabaza'
Nombre_Receta1 = 'Risotto de choclo'
Nombre_Receta2 = 'Risotto de atun'
# creacion
Recetas.append(Receta(Nombre_Receta, ingredientes))
Recetas.append(Receta(Nombre_Receta1, ingredientes))
Recetas.append(Receta(Nombre_Receta2, ingredientes))


def buscarReceta(nombre, lista):
    b = 0
    for x in lista:
        if nombre == x.nombre:
            b = 1
            print("La encontre")
            return lista.index(x)
    if b == 0:
        print("No se encontró esa receta.")
        return int(-1)

def buscarIngrediente(nombre, listaIngred):
    b = 0
    for x in listaIngred:
        if nombre == x.nombre:
            b = 1
            print("Lo encontre")
            return listaIngred.index(x)
    if b == 0:
        print("No se encontró ese ingrediente.")
        return int(-1)
    
def eliminarReceta(nombre, lista):
    
    index = buscarReceta(nombre, lista)
    if index != -1:
        lista.pop(index)
        print("Elemento eliminado.")

def modificarReceta(nombre, lista):
    recetaAModificar = buscarReceta(nombre, lista)
    if recetaAModificar != -1:
        opc = int(input("OPCIONES: \n 1-Modificar Nombre \n 2-Modificar ingrediente\nseleccion: "))
        if opc == 1:
            nombre = input('Ingrese un nuevo nombre para la receta: ')
            lista[recetaAModificar].nombre = nombre
            print("El nombre ha sido modificado")
        elif opc == 2:
            ingrediente = input('Ingrese el nombre del ingrediente a modificar: ')
            indexIng = buscarIngrediente(ingrediente, Recetas[recetaAModificar].ingredientes)
            
            if indexIng != -1:
                select = int(input("OPCIONES: \n 1-Modificar Nombre \n 2-Modificar cantidad\n3-Modificar unidad de medida \n0-Cancelar \nseleccion: "))
                
                if select == 1:
                        ingrediente_nuevo = input('Ingrese el nuevo nombre del ingrediente: ')
                        lista[recetaAModificar].ingredientes[indexIng].nombre = ingrediente_nuevo
                        print("Ingrediente ha sido modificado")
                elif select == 2:
                        cantidad_nueva = int(input('Ingrese la nueva cantidad del ingrediente: '))
                        lista[recetaAModificar].ingredientes[indexIng].cantidad = cantidad_nueva
                        print("Ingrediente ha sido modificado")
                elif select == 3:
                        medida_nueva = input('Ingrese la nueva unidad de medida del ingrediente: ')
                        lista[recetaAModificar].ingredientes[indexIng].unidadMedida = medida_nueva
                        print("Ingrediente ha sido modificado")
                elif select == 0:
                    print("Salida")
                    
                else:
                    print("opcion incorrecta.")
            else:
                print("No hay ningun ingrediente con ese nombre.")
            
        else:
            print('No se encontro la opcion...')
        
        


# mostrar
# for x in Recetas:
#     print(x.nombre)
# ## Todo funciona
# print(buscarReceta("Risotto de banana", Recetas))
#eliminarReceta(Nombre_Receta2, Recetas)

print(Recetas[1].ingredientes[1].nombre)
print(Recetas[1].ingredientes[1].cantidad)
print(Recetas[1].ingredientes[1].unidadMedida)

modificarReceta(Nombre_Receta1, Recetas)

print(Recetas[1].ingredientes[1].nombre)
print(Recetas[1].ingredientes[1].cantidad)
print(Recetas[1].ingredientes[1].unidadMedida)
