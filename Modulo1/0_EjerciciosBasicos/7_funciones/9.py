# Ejercicio 9
# Escribir una función que 
# calcule el máximo común divisor 
# de dos números y otra que calcule 
# el mínimo común múltiplo.

#5:51 pm 
#9:10 pm 


#lo ideal para resolver el ejercicio era hacerlo mas optimo
# estoy practicando la logica y intenté meter la 
# recursividad en ves de bucles

from math import trunc

Maximo_comun_Multiplo = []


def Maxicomo_comun(numeros):
    divisores1 = []
    divisores2 = []

    def mimi(A,B,C = 0 ):
        def Alpa(Num,lista):
            dato = Num[C]
            def fatakataka(dataso):
                Dataso2 = dato / dataso 
                if Dataso2 - trunc(Dataso2) == 0:
                    lista.append(Dataso2)

                if dataso == 0 or dataso == 1:
                    return 1
                return fatakataka(dataso-1)
            fatakataka(dato)

        if C == 0:
            Alpa(numeros,divisores1)
        elif C == 1:
            Alpa(numeros,divisores2)

        if A == 0 or A == 1:
            return 1
        return mimi(A-1,B,C+1)

    mimi(len(numeros),numeros)


    divisores2.sort()
    divisores1.sort()

    def Algoritmo_recursivo(A,B,C,D = 0):
        if B[A-1] in C:
            asd = trunc(B[A-1])
            Maximo_comun_Multiplo.append(asd)
            return 1
        if A == 0 or A == 1:
            return 1
        
        return Algoritmo_recursivo(A-1,B,C,D+1)
        
    Algoritmo_recursivo(len(divisores1),divisores1,divisores2)
    


Numeros1 = int(input("Ingrese el numero "))
Numeros2 = int(input("Ingrese el numero "))

Numeros = [Numeros1,Numeros2]

Maxicomo_comun(Numeros)
print(f"El Maximo comun divisor de {Numeros[0]} y {Numeros[1]} {Maximo_comun_Multiplo}")

# Minimo comun Multiplo
print(f"El minimo Comun Multiplo es {trunc(Numeros[0]*Numeros[1]/Maximo_comun_Multiplo[0])} ")


#la forma mas sencilla XD del ejercicio JAJJAJA
def mcd(n, m):
    
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
   
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))