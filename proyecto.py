#desarrollar clase de Receta y clase Ingrediente. 
#una receta va a recibir sus datos, entre ellos, ingredientes.

#ver si la lista de ingredientes puede llegar a ser una lista de diccionarios
#donde cada diccionario sea el ingrediente, es decir, contenga su nombre, unidad de medida y cantidad.
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

    def __init__(self, nombre, Listingredientes):
        """CONSTRUCTOR DE CLASE QUE RECIBE NOMBRE(str), INGREDIENTES(dicc del tipo Ingrediente), LISTA DE PASOS(str), IMAGEN DE PLATO
        TIEMPO DE PREPARACION(min), TIEMPO DE COCCION(min), ETIQUETAS (lista de palabras), FAVORITA (boolean)"""
        self.nombre = nombre
        self.ingredientes = []
        #recorrer cada dicc en la lista y transformarlo en una instancia de clase Ingrediente
        for ingred in Listingredientes:
            self.ingredientes.append(Ingrediente(ingred['nombre'], ingred['UnidadMedida'], ingred['cantidad']))

    def mostrar_ingredientes(self):
        """FUNCION PARA MOSTRAR LOS INGREDIENTES DE LA RECETA (provisorio creo)"""
        print(f"INGREDIENTES PARA PREPARAR: *{self.nombre}*")
        for ingrediente in self.ingredientes:
            ingrediente.__str__()

Nombre_Receta = 'Risotto de Calabaza'
ingredientes = [{'nombre': 'arroz','cantidad': 150,'UnidadMedida':'gr' },{'nombre':'Calabaza' ,'cantidad':200 ,'UnidadMedida':'gr' },{'nombre': 'cebolla','cantidad': 1,'UnidadMedida':'unidad' },
                {'nombre':'Caldo' ,'cantidad':0.5 ,'UnidadMedida':'litros' },{'nombre': 'vino blanco','cantidad': 1,'UnidadMedida':'vaso' },{'nombre':'manteca' ,'cantidad':1 ,'UnidadMedida': 'cucharita'},
                {'nombre':'Queso parmesano' ,'cantidad': 30,'UnidadMedida':'gr' },{'nombre': 'Sal','cantidad':1 ,'UnidadMedida':'cucharita'},{'nombre': 'Pimienta','cantidad': 1,'UnidadMedida': 'cucharita'}]
Risotto = Receta(Nombre_Receta, ingredientes)
Risotto.mostrar_ingredientes()
