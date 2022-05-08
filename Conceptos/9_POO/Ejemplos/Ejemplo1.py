# ejemplo de un cuadrado 
class Cuadadrado:
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

    def Area(self):
        area = self.ancho * self.alto
        return area
figura = Cuadadrado(10,20)
print(figura.alto,figura.ancho)
print(figura.Area())