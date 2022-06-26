# Ejercicio 5
# Escribir una función que calcule 
# el área de un círculo y otra que 
# calcule el volumen de un cilindro 
# usando la primera función.

def Calculo(radio,altura ,llave):
    def Volumen(radio,altura = 0):
        volumen =  3.1415 * radio**2 * altura
        print(f"El volumen del cilindro es {volumen}")
    def Area(radio):
        area = 3.1415 * radio**2
        print(f"El are de un circulo es {area}")
    if llave == 1:
        Volumen(radio,altura)
    else: 
        Area(radio)
 


decicion = int(input("que deseas calcular el volumen o el area escoge 1 o 2 "))

if decicion == 1:
    radio = int(input("Ingresa el radio >- "))
    altura = int(input("Ingresa la altura >- "))
    Calculo(radio,altura,1)
else:
    radio = int(input("Ingresa el radio >- "))
    Calculo(radio,0,2)