#poliformismo..............
class Auto:
    rueda = 4
    def dezplazamiento(self):
        print("El auto se está desplasando sobre 4 Ruedas")

class Moto:
    rueda = 2
    def dezplazamiento(self):
        print("La moto se esta desplasando sobre 4 ruedas")

##################
class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("Animal salvaje")

class Perro(Animales):
    def tipo_animal(self):
        print("Animal domestico")

Nuevo_animal = Leon("SIMBA")
Nuevo_animal.tipo_animal()

Nuevo_animal2 = Perro("REX")
Nuevo_animal2.tipo_animal()

        