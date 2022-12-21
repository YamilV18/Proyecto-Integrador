class Producto:
    """ Clase que construye producto """

    def __init__(self, codigo, nombre, precio, marca):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.precio: float = precio
        self.marca: str = marca
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} |".format(self.codigo, self.nombre, self.precio, self.marca))
