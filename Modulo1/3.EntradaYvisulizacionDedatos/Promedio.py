#Crea un programa que se llame Promedio.py, que pida 5 números, y calcula el promedio.

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
