#Reescribe el programa Saludar.py, usando la estructura condicional switch. 
#2/04/2022

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
        def lista(hola):
            horas = {
            0:"Buenas noches - Pero que haces despierto ves a dormir",
            24:"Buenas noches - Pero que haces despierto ve a dormir",
            1:"Buenas noches -  Pero que haces despierto ve a dormir ",
            2:"Buenas noches -  Pero que haces despierto ve a dormir ",
            3:"Buenas noches -  Pero que haces despierto es de madrugada ve a dormir ",
            4:"Buenos dias -  Pero que haces despierto  es de madrugada ve a dormir ",
            5:"Buenas dias -  Hoy será un gran dia",
            6:"Buenas dias -  Hoy será un gran dia",
            7:"Buenas dias -  Hoy será un gran dia",
            8:"Buenas dias -  Hoy será un gran dia",
            9:"Buenas dias -  Realiza las actividades",
            10:"Buenas dias -  Realiza las actividades",
            11:"Buenas dias -  Realiza las actividades",
            12:"Buenas dias -  Realiza las actividades",
            13:"Buenas tardes -  Como está la tarde",
            14:"Buenas tardes -  Como está la tarde",
            15:"Buenas tardes -  Como está la tarde ",
            17:"Buenas tardes -  Como está la tarde ",
            18:"Buenas tardes -  Como está la tarde ",
            19:"Buenas noches -  Como estuvo tu dia",
            20:"Buenas noches -  Como estuvo tu dia ",
            21:"Buenas noches -  Como estuvo tu dia ",
            22:"Buenas noches -  Ya es hora de dormir ",
            23:"Buenas noches -  Debes irte a dormir ",
            }  
            return horas.get(hola,"Que te pasa no ves que debes ingresar un numero solo dentro del rango")
        hola = horas_del_dia
        print(lista(hola))
                                                            
        
        print("Adios gracias por utilizarme")
        break


    except:
        print("Que te pasa obedece la orden")