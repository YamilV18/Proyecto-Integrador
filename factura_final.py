from persona import Persona
from producto import Producto
from factura_detalle import FacturaDetalle


class Facturafinal:
    """ Clase que implementa una factura"""

    def __init__(self, numero: int, cliente: Persona):
        
        self.numero: int = numero
        self.serie: str = f'F00{(self.numero)}'
        self.cliente: Persona = cliente
        self.producto: Producto
        self.base_imponible: float = 0.0
        self.igv: float = 0.0
        self.total: float = 0.0
        self.detalle: FacturaDetalle = []
        
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        print("---------------------------              -------------------")
        print("                                         |R.U.C: 20448844456")
        print("| LA TIENDITA DE DON PEPE |              |      FACTURA     ")
        print("| Ubicados en: Piura 156  |              |    ELECTRONICA   ")
        print("                                         ",format(self.serie))
        print("---------------------------              --------------------")
        print("")
        print("DATOS DEL CLIENTE:")
        print(f"DNI: {self.cliente.dni}")
        print(format(self.cliente.apellidos),", ",format(self.cliente.nombres))
        print(format(self.cliente.direccion))
        print("")
        print("| CÓDIGO | CANTIDAD | DESCRIPCIÓN | PRECIO UNITARIO | TOTAL |")
        print("-------------------------------------------------------------")
        #return print("| {} | {} | {} | {} | {} | {} |".format(self.numero, self.producto.nombre, self.producto.marca, self.base_imponible, self.igv, self.total))
        #print(f"                                     Subtotal: {self.base_imponible}")
        #print(f"                                     IGV: {self.igv}")
        #print(f"                                     Total: {self.total}")
        #return print("                                  Fecha: ",now.date())

    def convertir_a_string_final(self):
        print(f"                                     Subtotal: {self.base_imponible}")
        print(f"                                     IGV: {self.igv}")
        print(f"                                     Total: {self.total}")


    def agregar_detalle(self, producto: Producto):
        self.detalle.append(FacturaDetalle(producto))
    def calcular_igv(self):
        for detalle in self.detalle:
            self.base_imponible=self.base_imponible+detalle.base_imponible
            self.igv=self.igv+detalle.igv
            self.total=self.total+detalle.total
