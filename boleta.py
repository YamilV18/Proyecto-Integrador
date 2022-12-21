from boleta_detalle import BoletaDetalle
from persona import Persona
class Boleta:
    def __init__(self, numero, cliente):
        self.numero: int = numero
        self.serie: str = f'F00{(self.numero)}'
        self.cliente: Persona = cliente
        self.base_imponible: float = 0.0
        self.igv: float = 0.0
        self.total: float = 0.0
        self.detalle: BoletaDetalle = []
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):