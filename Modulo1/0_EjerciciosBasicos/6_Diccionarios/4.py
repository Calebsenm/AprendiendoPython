"""
Escribir un programa que 
pregunte una fecha en formato
 dd/mm/aaaa y muestre por pantalla 
 la misma fecha en formato dd de <mes> 
 de aaaa donde <mes> es el nombre del 
 mes.


finished 11_57:  16/06/2022
"""
# M = {
#     "dd":1,
#     "mm":1,
#     "aaaa":1
# }

# meses = ["Enero","Febrero","Marzo","Abril","Mayo","junio","julio","agosto","septiembre","octubre","noviembre","Diciembre"]

# day = input("please input the day separated by / ")
# hola = day.split("/")

# j = 0
# for i in M:
#     M[i]= hola[j]
#     j += 1


# a = M["mm"]
# print(a)
# Mese = meses[int(a)-1]
# print(f"dd {M['dd']} de {Mese} de {M['aaaa']} ")



    

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')

fecha = fecha.split('/')
print(f"Dia {fecha[0]} de {meses[int(fecha[1])]} del {fecha[2]}")