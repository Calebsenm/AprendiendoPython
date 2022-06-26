# Ejercicio 10
# Escribir una función 
# que convierta un número 
# decimal en binario 
# y otra que convierta un número 
# binario en decimal.

# Ya lo habia echo en el pasado etuvo easy 
# 25/06/2022
# 9:52 PM 

def Binario_decimal():
    Lista_Numeros = []
    Lista_Resultado = []
    numero = input("Ingresa el Numero Binario -> ")

    for i in range(len(numero)):
        Lista_Numeros.append(int(numero[i]))
    Lista_Numeros.reverse()

    o = 0
    for U in Lista_Numeros:
        Lista_Resultado.append(U*2**o)
        o += 1

    Binario = sum(Lista_Resultado)
    print(f"El numero decimal es > {Binario}")


def Decimal_binario():
    Lista_binario = []
    Valor = int(input("Ingresa un numero > "))

    Cociente = 1
    while Cociente != 0:
        Valor1 = Valor % 2
        Valor = Valor // 2
        Valor2 = str(Valor1)

        Cociente = Valor
        Lista_binario.append(Valor2)
    Lista_binario.reverse()
    Binario = "".join(Lista_binario)
    print(f"El numero binario es {Binario}")

    
deciones = {
    1:"Convertir Decimal A binario",
    2:"Binario a Decimal"
}

for i,J in deciones.items():
    print(i,J)

a = int(input("Ingresa que deseas elegir "))
if a == 1:
    Binario_decimal()

elif a == 2:
    Decimal_binario()