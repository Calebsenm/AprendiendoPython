"""
Ejercicio 8
 En una determinada empresa, sus empleados
  son evaluados al final de cada año. Los puntos 
   que pueden obtener en la evaluación comienzan 
    en 0.0 y pueden ir aumentando, traduciéndose en
   mejores beneficios. Los puntos que pueden conseguir
  los empleados pueden ser 0.0, 0.4, 0.6 o más, pero 
no valores intermedios entre las cifras mencionadas.
  A continuación se muestra una tabla con los niveles
   correspondientes a cada puntuación. La cantidad de
    dinero conseguida en cada nivel es de 2.400€ multiplicada 
     por la puntuación del nivel.

nivel 
Inaceptable     0.0
Aceptable       0.4
Meritorio       6.6 +

finikitado está aburrido XD 9/05/2022
"""
from re import A


Dinero = 2400
Inaceptable = 0.0
Aceptable = 0.4 
Meritorio = 0.6
nivel = ""

print("La puntuacion permitida es 0 , 0.2  o 0.6")
puntuacion = float(input("Ingresa la puntuacion >> "))

def Texto():
    print(f"Tu nivel de rendimiento es {nivel} \n Te corresponde {Dinero * puntuacion}$")

if puntuacion == Inaceptable:
    nivel = "Inaceptable"
    Texto()
elif puntuacion == Aceptable:
    nivel = "Aceptable"
    Texto()
elif puntuacion == Meritorio:
    nivel = "Meritorio"
    Texto()
    

else:
    print("Error")


    







