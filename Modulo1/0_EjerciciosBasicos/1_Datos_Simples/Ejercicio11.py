"""
Imagina que acabas de 
abrir una nueva cuenta de 
ahorros que te ofrece el 4% 
de interés al año. Estos ahorros 
debido a intereses, que no se cobran 
hasta finales de año, se te añaden al 
balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo 
la cantidad de dinero depositada en la cuenta 
de ahorros, introducida por el usuario. Después 
el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y 
tercer años. Redondear cada cantidad a dos decimales.

finikitado el 1/05/2022
"""



Interes = 4
Cuenta_Deahorros = int(input("Deposita tu Dinero >> "))

Años = 3
a = 1
while a <= Años:
    Cuenta_Ahorros = Cuenta_Deahorros * Interes / 100 + Cuenta_Deahorros
    Cuenta_Deahorros = Cuenta_Ahorros
    print(f"Tu cuenta de ahorros en el año {a} Es de {Cuenta_Deahorros:.2f}$")
    
    a = a + 1 

