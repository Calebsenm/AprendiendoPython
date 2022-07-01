#super () = Funtion used to give acces to the 
#           methods of a parent class.
#           Return a temporary objet of a parent
#           class when used



class Recatngle():
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.widht = width

class Square(Recatngle):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)
    
    def Area(self):
        return self.lenght * self.widht


class Cube(Recatngle):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)
        self.height = height

    def Volumen(self):
        return self.lenght * self.widht * self.height
        
# -----------------------------------------
square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.Area())
print(cube.Volumen())

