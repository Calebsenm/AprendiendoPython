#clase y estatico


import math

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
    def __repr__(self):
        return f"pastel ({self.ingredientes !r})"

    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina","leche","chocolate"])

    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina","leche","vainilla"])     

print(Pastel.Pastel_chocolate())


#static method

class Galleta:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def __repr__(self):
        return(f"Galleta([{self.ingredientes},"f"{self.tamaño}])")
    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi
    
Nueva_galleta = Galleta(["Arina","Leche","Azucar","Crema"],4)
print(Nueva_galleta.ingredientes)
print(Nueva_galleta.tamaño_area(2))