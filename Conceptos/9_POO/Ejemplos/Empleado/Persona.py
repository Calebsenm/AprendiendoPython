class Persona:
    def __init__(self,nombre,apellido,dni,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
    def __str__(self) :
        return f"{self.nombre} \n {self.apellido} \n {self.dni} \n {self.telefono}"
        
        