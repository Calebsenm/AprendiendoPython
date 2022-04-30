#ejemplo de erencia

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    def ingresardato(self):
        self.datos = [int(input("ingrese Datos" + str(i+1)+ "= ")) for i in range(self.n)]

class Operaciones(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def suma(self):
        a,b = self.datos
        s = a + b

        print("el resultado es: ",s)

    def Resta(self):
        a,b = self.datos
        r = a - b

        print("el resultado es: ",r)
    
    def Mult(self):
        a,b = self.datos
        m = a * b

        print("el resultado es: ",m)
    
class raiz (Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def cuadrada(self):
        import math
        a, = self.datos
        print("EL resultado es: ",math.sqrt(a))

objeto = Operaciones()
#compruebla la herencia
print(isinstance(objeto,raiz))

objeto2 = Operaciones()
print(issubclass(Calculadora,Operaciones))

print(issubclass(raiz,Calculadora))