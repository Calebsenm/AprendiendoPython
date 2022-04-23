"""
Crea un archivo con el nombre Calculadora Funciones.py.
3. Realiza las funciones de Caja blanca con cada una de 
las operaciones de la calculadora. Suma, Resta, 
Multiplicación, Logaritmo, Coseno, Seno, Raíz 
cuadrada, convertir Decimal a binario y Binario a 
decimal. Recuerda incluir la validación de las operaciones.
"""


import math
from os import system
import time

####################################################################
def suma():
    system("cls")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = numero1 + numero2
    print(f"la suma es: {operacion}")
    time.sleep(3)

def resta():
    system("cls")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = numero1 - numero2
    print(f"la resta es: {operacion}")
    time.sleep(3)

def multiplicacion():
    system("cls")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = numero1 * numero2
    print(f"la la multiplicacion es: {operacion}")
    time.sleep(3)

def Logaritmo():
    system("cls")
    print("logaritmo")
        
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = math.log(numero1,numero2)    
    print(f"EL logaritmo del nuemero {numero1+numero2} es >> {operacion} ")

    time.sleep(3)

def Coseno():
    
    system("cls")
    print("Coseno")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = math.cos(numero1 + numero2)

    print(f"El coseno  de {numero2+numero1} es  {operacion}")

    time.sleep(3)
def Seno():
    system("cls")
        
    print("Seno")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))
    operacion = math.sin(numero1 + numero2) 
    print(f"EL seno de {numero1 + numero2}  es {operacion}")

    time.sleep(3)

def Raiz():
    system("cls")

    print("Raiz cuadrada")
    numero1 = int(input("Por favor ingresa un numero >>> "))
    numero2 = int(input("Por favor ingresa el siguiente numero >>"))

    operacion = math.sqrt(numero1 + numero2)
    print(f"La raiz cuadrada de {numero1 + numero2} es la siguiente {operacion}")

    time.sleep(3)

def Deccimal_binario():
    system("cls")

    print("has elegido convertir a binario: ")
    valor = int(input("ingresa el numero que deseas convertir en binario >>> ") )

    #aquí se convierte los numeros a binarios
    M2=[]
    cociente = 1


    while cociente != 0:
        valor2 = valor %2
        valor = valor //2
        valor1 = str(valor2)           
        M2.append(valor1)
            
        cociente = valor
    M2.reverse()

    # se imprimes in coorchetes
    lista = "".join(M2)
    print(f"Tu numero binario es el siguiente >>>>>>  {lista}  <<<<<<<")

    time.sleep(3)

def Binario_Decimal():
    system("cls")
    print("has elegido la opcion convertir de binario a decimal ")

    #pide el nummero luego lo invierte y lo almacena en una lista liengo va iterando la lista y va multiplicando cada numero por 2*i y luego se suma toda la lista
    dato = input("Ingrese un nuemero binario >>>> ")

    Lista = []
    contar = len(dato)
        
    for i in range(contar):
        Lista.append(int(dato[i]))


    Lista.reverse()
    count = len(Lista)

    lISTA = [] 

    print
    for i in range(count):
        lISTA.append(Lista[i]*2**i)
                           
    Suma_lita = sum(lISTA)

    print(f"El numero decimal es >>> {Suma_lita}")

    time.sleep(10)

######################################################################################################
system("cls")
#la lista 
M = ["1 Suma","2 Resta","3 Multiplicacion","4 Logaritmo","5 Coseno","6 Seno","7 Raiz cuadrada","8 Decimal a binario","9 Binario a decimal"]

while True:
    system("cls")
    for i in range (9):
        print(M[i])
    desicion = int(input("ingresa el numero de la operacion que desas realizar >> "))
    

    if desicion == 1:
        suma()

    elif desicion == 2:
        resta()

    elif desicion == 3:
        multiplicacion()

        
    elif desicion == 4:
        Logaritmo()
    elif desicion == 5:
        Coseno()

    elif desicion == 6:
        Seno()


    elif desicion == 7:
        Raiz()
        
    elif desicion == 8:
        Deccimal_binario()
            
    elif desicion == 9:
        Binario_Decimal()
##########################################################################################################################
        








