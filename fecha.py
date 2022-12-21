class Fechas:
    def __init__(self,numero,dia,mes,año,hora,minuto):
        self.numero:int=numero
        self.dia=dia
        self.mes=mes
        self.año=año
        self.hora=hora
        self.minuto=minuto
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print(f"Fecha: {self.dia}-{self.mes}-{self.año}  {self.hora}:{self.minuto}")