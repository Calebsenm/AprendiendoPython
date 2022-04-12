"""
2. Reescriba el código de ejercicios previos
en el mismo programa, para: Saludar, Calcular 
si un número es par, Calcular el promedio de 5 notas, 
Calcular el módulo, Calcular el porcentaje y elevar
a una potencia. Graba el programa como Ciclos.py

3. Organiza las funcionalidades anteriores en bloque, 
de la siguiente forma: 1. Saludar, 2. Es par, 3. Promedio, 
4. Módulo, 5. Porcentaje, 6. Potencia 0. Salir

4. Crea una variable centinela, 
la cual será pedida al usuario, 
para que sea ingresada por la consola, 
según la operación del menú de opciones, 
la cual será la selección a ejecutar.

5. Usa un ciclo para imprimir las opciones. 
El programa debe terminar si el usuario ingresa 0.

6. Organiza el código para que solo se 
ejecuten las instrucciones correspondientes 
a la selección del usuario.

7. Usando un switch o un if anidado, 
crea la lógica necesaria para que se 
ejecuten los procedimientos, dependiendo 
del valor centinela.

8.Se deben validar los datos de entrada 
para evitar errores en la interacción del 
usuario.

9. Realiza el mismo menú cambiando de 
ciclo, es decir, si lo hiciste con un 
ciclo while, cambia a un ciclo do-while, 
o a un ciclo for.

10. Agrega un nuevo procedimiento
 al menú, luego publica el código 
 y las evidencias con los cambios 
 planteados, en el foro: Taller 
 estructura de control y ciclos.



el ejercicio empezo a desarrollarse a  las       10:25 pm  el 11/abril/2022
Ejercicio terminado a las                        11:02 pm  el 11/abril/ 2022


"""

from os  import system
system("cls")



# funcion del la opcion saludo
def Saludo ():
    system("cls")
    HORAS = [   "0 = 12:AM","1 = 1:AM","2 = 2AM","3 = 3:AM","4 = 4:AM",
                "5 = 5:AM","6 = 6:AM","7 = 7AM","8 = 8:AM","9 = 9:AM",
                "1O = 10:AM","11 = 11:AM","12 = 12PM","13 = 1:PM","14 = 2:AM",
                "15 = 3:PM","16 = 4:PM","17 = 5PM","18 = 6:PM","19 = 7:PM",
                "20 = 8:PM","21 = 9:PM","22 = 10:PM","23 = 11:PM","24 = 12:AM"
                
    ]
    print("Esta es tu tabla de las horas")
    for i in range(25):
        print(HORAS[i],end=' ')
        print()

    print("¿Quieres que te salude? ")
    print("Solo ingresa un numero del 0 al 24")
    print("arriba tienes la lista de horas para ingresar")


    while True: 
        try:
            
            horas_del_dia = int(input("Ingresa tu hora: ") )
            if horas_del_dia <0 or horas_del_dia >24:
                system("cls")
                print("Que te pasa no ves que debes ingresar un numero solo dentro del rango")
            elif horas_del_dia >= 0 and horas_del_dia <= 2:
                system("cls")
                print("Pero que haces despierto ves a dormir")
                print("Buenas noches")
            elif  horas_del_dia <= 4 and horas_del_dia >= 3 :
                system("cls")
                print("Que haces despierto? es de madrugada")
                print("Buenos dias")
            elif horas_del_dia >= 5 and horas_del_dia <= 8:
                system("cls")
                print("Hoy será un gran dia")
                print("Buenos dias")
            elif horas_del_dia >= 9 and horas_del_dia <= 12:
                system("cls")
                print("Estas desarrollando las actividades verdad?")
                print("Buenos dias")
            elif horas_del_dia >= 13 and horas_del_dia <= 18:
                system("cls")
                print("Como te va? hace sol o no")
                print("Buenas Tardes")
            
            elif horas_del_dia >= 19 and horas_del_dia <= 22:
                system("cls")
                print("Como estuvo tu dia? ")
                print("Buenas  noches")
            elif horas_del_dia >= 23 and horas_del_dia <= 24:
                system("cls")
                print("Que haces despierto? ¡Ves a dormir!")
                print("Buenas noches")
            
            
            print("Adios gracias por utilizarme")
            break


        except:
            print("Que te pasa obedece la orden")

#funcion si el numero es par
def Par():
    print("Vienvenido al programa")
    while True:
        try:
            print("si deseas terminar el progrma ingresa 0 ")
            Dato = int(input ("Porfavor ingresa un valor un numero: "))
            Dato2 =  Dato % 2

            if Dato == 0:
                break
            if Dato2 == 0:
                print("EL numero ingresado es par")
            
            else:
                print("El numero ingresado es impar")

        except ValueError:
            print("el valor no esta permitido")


# la funcion de promedio
 
def Promedio():
    
    print("Welcome to the math notes hahha")

    M = [0,0,0,0,0]
    a = 0
    b = 1
    c = 0


    # Pide los datos y los ingresa a la lista

    while a < 5:

        try:
            
            valor = float(input(f"Ingresa la nota1 {b}: "))
            if valor >= 0 and valor <=6:
                M [a] = valor
            else:
                a = a - 1
                b = b - 1
        except ValueError:
            print("EL numero es incorrecto")
            a = a-1
            b = b-1

        a = a + 1 
        b = b + 1
        
    Valor1 = M[0] 
    Valor1 += M[1]
    Valor1 += M[2]
    Valor1 += M[3]
    Valor1 += M[4]

    Valor1 = Valor1/5

    if Valor1 >=0 and Valor1 <3 :
        
        print("Que Haces con tu vida")
        print("Ponte a estudiar")

    elif Valor1 >= 3 and Valor1 <4:
        print("Felicidades has ganado la materia")
        print("tu nota es basica ponte a estudiar mas!")

    elif Valor1 >= 4 and Valor1 <5:
        print("Felicidades has ganado la materia")
        print("Tu nota es exelente")
    elif Valor1 == 5:
        print("tu nota ha sido una de las mejores ")

    print(Valor1)

# funcion del modulo 

def Modulo():
        
    for i in  range(101):
        Modulo = i % 3
        print(f"El modulo Del numero {i} Dividido entre 3 es: {Modulo}")


# funcion porcentaje

def Porcentaje():
    
    CantidadDeAlumnos = 600
    for i in range(10,101,10):

        porcentaje = CantidadDeAlumnos * i /100
        a = round(porcentaje)
        print(f"El {i}% de los alumnos 600 alumnos es: {a} ")
        

# funcion de potencia 

def Potencia():
    while True:  
        try:
                
            PrimerNumero = int(input("Ingresa un numero: "))

            if PrimerNumero > 100:
                print("EL dato es muy alto para ingresar")
            if PrimerNumero < 0  or PrimerNumero <101:
                NumeroDos = int(input("Ingresa el numero que sera la potencia: "))
                if NumeroDos >10:
                    print("EL valor es superior debe ingresar  un numero menor")
                elif NumeroDos <11:
                    resultado = PrimerNumero ** NumeroDos
                    print(f"La el resulytado del operacion es: {resultado}")
                    break

        except ValueError:
            print("NO seas nood le piden un nuemero")

# La estructura del programa :D 

M = ["1. Saludar","2. Es par","3. Promedio","4. Módulo","5. Porcentaje","6. Potencia","0. Salir"]
a = 0

while True:
    
    try:
        
        while a < 7:
            print (M[a])
            a = a + 1 

        centinela = int(input("Elige una eleccion: "))
        if centinela >6 or centinela <0:
            print("Dato no esta permitido")
        

        elif centinela == 0:
            exit()
        elif centinela == 1: 
            Saludo()
            a = 0
        elif centinela == 2:
            Par()
            a = 0
            
            
            
        elif centinela == 3:
            Promedio()
            a = 0
            


        elif centinela == 4:
            Modulo()
            a = 0

        elif centinela == 5:
            Porcentaje()
            a = 0

        elif centinela == 6:
            Potencia()
            a = 0


    except ValueError:
        print("la opcion es incorrecta ")

