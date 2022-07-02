from http import client
from Empleado import Empleado
from Cliente import Cliente


Personas = []

def Guarda():
    Respuesta = input("Si desea agregar un empleado imgrese 0 Si desea imgresar un cliente ingrese 1>> ")
    nombre = input("ingresa el nombre >> ")
    apellido = input("ingresa el apellido >> ")
    dni = input("ingresa el dni >> ")
    numero = input("ingresa el numero >> ")

    if Respuesta == "0":
        salario = input("Ingrese el salario")
        Empleado1 = Empleado(nombre,apellido,dni,numero,int(salario))
        
        Personas.append(Empleado1)

    elif Respuesta == "1":
        rango = input("ingrese el rango ")
        Cliente1 = Cliente(nombre,apellido,dni,numero,rango)
        
        Personas.append(Cliente1)

Guarda()
Guarda()


for persona in Personas:
    print(persona)