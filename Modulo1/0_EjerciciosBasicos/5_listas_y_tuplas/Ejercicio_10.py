# Ejercicio 10
# Escribir un programa que almacene 
# en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre 
# por pantalla el menor y el mayor de los precios.

#easy   3:21 pm   13/06/2022

M = [50, 75, 46, 22, 80, 65, 8]
print(M)
#el algoritmo de ordenamiento xd
U = 0
U1 = 1

iterator = 1
iterator1 = 1
while iterator1 != len(M):
    while iterator != len(M):
        if M[U] > M[U1]:
            A = M[U] 
            M[U] = M[U1]
            M[U1] = A

            U += 1
            U1 += 1
        else:
            U += 1
            U1 += 1
        
        iterator +=1
    U = 0
    U1 = 1
    iterator = 1
    iterator1 += 1

print(M)
print(f"EL precio menor es {M[0]} \nEl precio Mayor es {M[-1]}")



#The tutor

# prices = [50, 75, 46, 22, 80, 65, 8]
# min = max = prices[0]
# for price in prices:
#     if price < min:
#         min = price
#     elif price > max:
#         max = price 
# print("El mínimo es " + str(min)) 
# print("El máximo es " + str(max))