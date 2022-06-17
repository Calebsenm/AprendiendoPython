# jercicio 2
# Escribir un programa que 
# pregunte al usuario su nombre, 
# edad, dirección y teléfono y lo 
# guarde en un diccionario. Después 
# debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en 
# <dirección> y su número de teléfono es 
# <teléfono>.

#easy wiwiwiiwiwiwiiwiwiwi
#15/06/202  - 10:28 am xd 

Dates = []
M = ["please input your name  ","please input your age ","plese input your addres ","Plese input your phone number "]
N = ["name","age","addres","number"]
Diccionary = {}

for i in M:
    date = input(i)
    Dates.append(date)

p = 0
for i in N:
    Diccionary[i] = Dates[p]
    p += 1

print(Dates)
print(Diccionary)
for i in Diccionary:
    print(f"your {i} is {Diccionary[i]}")