#Metodos...
#self

class Matematias:
    def Suma(self):
        self.numero1 = 1
        self.numero2 = 2

    def Resta(self):
        self.numero1 = 6
        self.numero2 = 3

b = Matematias()
b.Suma()
s = Matematias()
s.Resta()

print(b.numero1 + b.numero2)
print(s.numero1 - s.numero2)

"""
3
3
"""