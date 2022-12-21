class FacturaDetalle:
    """ Clase que construye el detalle de una factura """

    def __init__(self, codigo, nombre, marca, cantidad, precio):
        self.codigo:str = codigo
        self.nombre:str = nombre
        self.marca:str = marca
        self.cantidad:float = cantidad
        self.precio:float = precio
        #self.base_imponible:float = (self.precio*self.cantidad)/1.18
        self.base_imponible:float = self.precio*self.cantidad
        self.igv:float = ((self.precio*self.cantidad)*1.18)-self.base_imponible
        self.total:float = (self.precio*self.cantidad)*1.18
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} - {} | {} | {} |".format(self.codigo, self.cantidad, self.nombre, self.marca, self.precio, self.base_imponible))
