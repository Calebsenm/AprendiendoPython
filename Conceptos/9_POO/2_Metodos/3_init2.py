
class Calculadora:
    def __init__(self,numero1,numero2):
        self.suma = numero1 + numero2
        self.resta = numero1 - numero2
        self.multiplicacion = numero1 * numero2
        self.division = numero1 / numero2

Operacion = Calculadora(5,3)
print(Operacion.suma)
print(Operacion.resta)
print(Operacion.multiplicacion)
print(Operacion.division)

"""
8
2
15
1.6666666666666667
"""
