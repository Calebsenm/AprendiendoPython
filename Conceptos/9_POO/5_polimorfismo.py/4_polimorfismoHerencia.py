class Aves:
    def volar(self):
        print("La mayoria de las haves pueden volar")

class Aguila(Aves):
    def volar(self):
        print("Las aguilas pueden volar")

class Gallina(Aves):
    def volar(self):
        print("la gallina no puede volar")

objeto_ave = Aves()
objeto_aguila = Aguila()
objeto_gallina = Gallina()


objeto_ave.volar()
objeto_aguila.volar()
objeto_gallina.volar()