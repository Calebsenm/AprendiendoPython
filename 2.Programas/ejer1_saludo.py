#Realiza el diseño de un programa que salude según la hora del día

from os import system
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