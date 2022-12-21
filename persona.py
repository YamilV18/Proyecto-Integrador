class Persona:
    """Clase que construye persona"""

    def __init__(self, dni, nombres, apellidos, direccion, telefono) -> None:
        self.dni:str = dni
        self.nombres:str = nombres
        self.apellidos:str = apellidos
        self.direccion:str = direccion
        self.telefono:str = telefono
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} |".format(self.dni, self.nombres, self.apellidos, self.direccion, self.telefono))
