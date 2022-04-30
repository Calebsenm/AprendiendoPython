#metodo

class Mamifero:
    def __init__(self,nombre):
        print(nombre, "es un animal de sangre caliente")

class Leon(Mamifero):
    def __init__(self):
        print("el leon en un animal de cuatro patas")

        super().__init__("simba")
        #Mamifero.__init__(self,"simba")

nuevo_leon = Leon()