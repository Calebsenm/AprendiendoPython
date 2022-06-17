"""
Escribir un programa que 
pregunte una fecha en formato
 dd/mm/aaaa y muestre por pantalla 
 la misma fecha en formato dd de <mes> 
 de aaaa donde <mes> es el nombre del 
 mes.


finished 11_57:  16/06/2022
"""
M = {
    "dd":1,
    "mm":1,
    "aaaa":1
}

meses = ["Enero","Febrero","Marzo","Abril","Mayo","junio","julio","agosto","septiembre","octubre","noviembre","Diciembre"]

day = input("please input the day separated by / ")
hola = day.split("/")

j = 0
for i in M:
    M[i]= hola[j]
    j += 1


a = M["mm"]
print(a)
Mese = meses[int(a)-1]
print(f"dd {M['dd']} de {Mese} de aaaa {M['aaaa']} ")

print(M)

    