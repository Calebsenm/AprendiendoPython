# Ejercicio 2
# Escribir una función que simule una calculadora 
# científica que permita calcular el seno, coseno, 
# tangente, exponencial y logaritmo neperiano. 
# La función preguntará al usuario el valor y la función a 
# aplicar, y mostrará por pantalla una tabla con los enteros 
# de 1 al valor introducido y el resultado de aplicar 
# la función a esos enteros.


#5:00pm   26/06/2022 
#7:00pm   26/06/2022               me tarde por que me puse a inventar con un diccionario como condicional 

from math import sin, cos, tan, exp, log

Valores = {}

def ciclo(A,B):
    for i in range(B):
        Valores[i+1] = A(i+1)
    

def seno(numero):

    ciclo(sin,numero)
   

def coseno(numero1):
    ciclo(cos,numero1)
  

def tangente(numero2):
    ciclo(tan,numero2)
    

def exponencial(numero3):
    ciclo(exp,numero3)
    

def nerperiano(numero4):
    ciclo(log,numero4)
    

def opcion(a,b):
    if a == 1:
        J = seno(b)
    if a == 2:
        J = coseno(b)
    if a == 3:
        J = tangente(b)
    if a == 4:
        J = exponencial(b)
    if a == 5:
        J = nerperiano(b)
    return J


opciones = {1:"seno",2:"coceno",3:"tangente",4:"exponencial",5:"logaritmo nerperiano"}
for i,j in opciones.items():
    print(i,j)
operacion = int(input("Ingresa el numero dela opcion -> "))
numero = int(input("Ingresa el numero -> "))


opcion(operacion,numero)

for i,j in Valores.items():
    print(i,"->",j)