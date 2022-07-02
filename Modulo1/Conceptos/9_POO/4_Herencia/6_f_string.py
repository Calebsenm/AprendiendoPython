#otra forma de concadenacion.............
#f- string
# format %

#esto es para imprimir las cadenas y valores metidos
"""
curso = "python"
print("tutoriales de %s"%curso)

nombre = "victor"
edad = 17

print("hola soy, %  s y tengo % s años..."%(nombre,edad))

"""
"""
tutoriales de python
hola soy, victor y tengo 17 años...
"""

"""

print("hola {} tu tienes {}".format(nombre,edad))

print(f"hola {edad} tienes {edad}")

"""

#f-string

from tkinter import N
from numpy import obj2sctype


class Estudientes:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad  = edad
    
    def __str__(self):
        return f"hola soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante = Estudientes("victor","cruz",17)
print(f"{nuevo_estudiante}")

class Tarros:
    def __init__(self,tamaño,capacidad,forma):
        self.tamaño = tamaño
        self.capacidad = capacidad
        self.forma = forma
    def __repr__(self) -> str:
        return f"hola soy un tarro de {self.tamaño} con una capacidad de {self.capacidad} y una forma {self.forma}"

nuevo_tarro = Tarros("30cm","200 cm**2","circular")
print(f"{nuevo_tarro !r}")

Tarro2 = Tarros("20","100**2","Cuadrado")
print(f"{Tarro2 !r}")