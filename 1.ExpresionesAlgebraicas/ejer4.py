"""
4. Dada una ecuación algebraica de 4 incógnitas, codifica la expresión en 
partes simples y desarrolla la ecuación en un archivo con nombre ecuacion.py

a. Calcula su resultado evaluado con valores constantes para las incógnitas.

b. Cambia los valores constantes de las incógnitas, compile y revise el resultado.

"""
"""
para resolver la ecuacion:


"""

# se ingresa la ecuacion algebraica
#ingreso opara imgresar la ecuaciones y valida que se hayan ingresado todas ?        listo
#ingreso de cada ecuacion por separado                                               trabajando en ello

from os import system


#Funcion de ingreso de los datos de la ecuacion
def eleccion():
    while True:
        system("cls")
        print("las ecuaciones estan formadas de incognitas")
        valor1= input("ingresa el valor 1 de la  ecuacion: " )
               
        valor2= input("ingresa el valor 2 de la  ecuacion: ")
                
        valor3= input("ingresa el valor 3 de la  ecuacion: ")
                
        valor4= input("ingresa el valor 4 de la  ecuacion: ")
                
        valor5 = "="

        valor6 = input("ingresa el resultado: ")
                

        print("TU ecuacion queda formulada de la siguiente manera : ")

        print(valor1," ",valor2," ",valor3," ",valor4," ",valor5," ",valor6)

        print("Si deseas guardar y salir ingresa       1")
        print("Si deseas modificar la ecuacion ingresa 2")
        eleccion = int(input ("Que deseas elegir?: "))

        if eleccion == 1:
            break
        else:
            continue   
    if EleccionesDelasEcuaciones == 0:
        N[0][0]= valor1
        N[0][1]= valor2
        N[0][2]= valor3
        N[0][3]= valor4
        N[0][5]= valor6

        
    elif EleccionesDelasEcuaciones ==1:
        N[1][0]= valor1
        N[1][1]= valor2
        N[1][2]= valor3
        N[1][3]= valor4
        N[1][5]= valor6
        print("2")
    elif EleccionesDelasEcuaciones ==2:

        N[2][0]= valor1
        N[2][1]= valor2
        N[2][2]= valor3
        N[2][3]= valor4
        N[2][5]= valor6
        print("3")
    elif EleccionesDelasEcuaciones ==3:

        N[3][0]= valor1
        N[3][1]= valor2
        N[3][2]= valor3
        N[3][3]= valor4
        N[3][5]= valor6
        print("4")
    
#varibles inportantes
M = 0

N = [   ["0","0","0","0","=","0"],
        ["0","0","0","0","=","0"],
        ["0","0","0","0","=","0"],
        ["0","0","0","0","=","0"],
]
numeroingresado = 0
EcuacionesFaltanetes = ["Ecuacion1","Ecuacion2","Ecuacion3","Ecuacion4"]

#variables de toma de deciciones
VerificaIngreso = 0
Desicion2Eleccion = 0
EleccionesDelasEcuaciones = 0


while  True:
    if Desicion2Eleccion == 0:
        
        system("cls")
    

    print("ELige 1 para ingresar la ecuacion")
    print("Elige 2 para calcular la ecuacion")

    Decicion = int(input("Que deseas elegir?: "))

    if Decicion ==1:
        while True: 
            VerificaIngreso = 1
            system("cls")
            Elecciones = ["Para ingresar la ecuacion 1 ingresa 1 ","Para ingresar la ecuacion 2 ingresa 2 ","Para ingresar la ecuacion 3 ingresa 3 ","Para ingresar la ecuacion 4 ingresa 4 ",]
            for i in Elecciones:
                print(i)

            while True:
                
                if numeroingresado <=4:
                    print(f"te falta ingresar las ecuaciones {EcuacionesFaltanetes}")
                if EcuacionesFaltanetes == []:
                    print("Has ingresado todas las ecuaciones con exito")
                    break


                #se ingresa  a la opcion para ingresar la ecuacion
                Deciciones = int(input("ingresa la ecuacion que deseas ingresar: "))
                if Deciciones ==1:
                    

                    eleccion()
                    system("cls")
                    print("has ingresado la ecuacion n1 con exito")
                    numeroingresado = numeroingresado+1
                    EleccionesDelasEcuaciones = 1
                    EcuacionesFaltanetes.remove("Ecuacion1")
                    
                elif Deciciones ==2:

                    eleccion()
                    system("cls")
                    print("has ingresado la ecuacion  n2 con exito")
                    numeroingresado = numeroingresado+1
                    EcuacionesFaltanetes.remove("Ecuacion2")
                    EleccionesDelasEcuaciones = 2
                    
                elif Deciciones ==3:
                    eleccion()
                    system("cls")
                    print("has ingresado la ecuacion n3 con exito")
                    numeroingresado = numeroingresado+1
                    EcuacionesFaltanetes.remove("Ecuacion3")
                    EleccionesDelasEcuaciones = 3
                elif Deciciones == 4:
                    eleccion()

                    system("cls")
                    print("has ingresado la ecuacion n4 con exito")
                    numeroingresado = numeroingresado+1
                    EcuacionesFaltanetes.remove("Ecuacion4")
                    EleccionesDelasEcuaciones = 4

                else:
                    break
                if numeroingresado ==4:
                    break

            break   
            
    
    #Ejecuta la opcion2
    elif Decicion ==2:
        Desicion2Eleccion = 1 

        if VerificaIngreso ==0:
            system("cls")
            print("No has ingresado la ecuacion")
            continue
        elif VerificaIngreso ==1:
            print("Tu ecuacciones son las siguientes: ")
            for i in N:
                print(i)
        

        # SE desarrolla la logica para hacer la ecuacion:
        



    else:
        break
