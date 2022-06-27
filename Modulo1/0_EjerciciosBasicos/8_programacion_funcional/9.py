"""
Ejercicio 9
Escribir una función que calcule el módulo de un vector.

"""
# 11:40  AM   27/06/2022

# Me 
def Modul_Vector(A,B = 0):
    return pow(A**2 + B**2,0.5)

print(Modul_Vector(4,2))


# Solition 2 

def h(A):
    return sum([k **2 for k in A ]) ** 0.5
print(h((2,2,1,6,2)))



