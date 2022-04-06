#Dia de desarrollo 30 - 1 de marzo del 2022 a las 12:40 fue termino         casi un total de
# 4 horas de desarrollo aproximadamente

#Elabora un programa de un programa que calcule una devuelta sobre una compra, con un valor constante.

#imprime la lista de objetos
def imprime():
    
    C = 0
    D = 0
    while C<5: 
        while D <2 :
            print(M[C][D])
            D  = D + 1
        C = C+1
        D = 0





from os import system
system("cls")
M = [

    ["Arroz = 1000$","Pan = 500$"],
    ["Tomate = 500$","Cebolla = 500$"],
    ["Papa = 1000$","Frijol = 2000$"],
    ["Agua = 100$","Bonbombum = 200$"],
    ["Banano = 1000$","Aguacate = 2000$"]
]
Obtos_ALmacen=["Arroz","Pan","Tomate","Cebolla","Papa","Frijol","Agua","Bombombum","Banano","Aguacate","Guardar"]
COMPRA =[]
imprime()
Rango_Var = 1
# introduce los objetos y los imprime

print("Que deseas comprar? ")
while True:
    
    Objeto = input("Elige un producto: ")
    if Objeto in Obtos_ALmacen:

        print("El objeto esta en la lista")

        COMPRA.append(Objeto)

        system("cls")
        imprime()

        print("SI deseaas guardar la lista de objetos ingresa la palabra Guardar")
        print("Esta es la lista de objetos a comprar")
        ###################################
        
        for i in range(Rango_Var):
            print(COMPRA[i])

        Rango_Var = Rango_Var +1 
       
        ###################################         
        if Objeto == "Guardar":
            break

    
    else:
        print("El objeto no se encuentra en la lista")

   
#se ingresa el pago
            ###
system("cls")
print("Estos son los objetos que ha elegido")
COMPRA.remove("Guardar")

cantidad = len(COMPRA)

for I in range(cantidad):
    print(COMPRA[I])


valor_cuenta = 0

if "Arroz" in COMPRA:
    valor_cuenta += 1000
if "Pan" in COMPRA:
    valor_cuenta += 500
if "Tomate" in COMPRA:
    valor_cuenta += 500
if "Cebolla" in COMPRA:
    valor_cuenta += 500
if "Papa" in COMPRA:
    valor_cuenta += 1000
if "Frijol" in COMPRA:
    valor_cuenta +=2000
if "Agua" in COMPRA:
    valor_cuenta +=100
if "Bombombum" in COMPRA:
    valor_cuenta +=200
if "Banano" in COMPRA:
    valor_cuenta += 1000
if "Aguacte" in COMPRA:
    valor_cuenta += 2000


print(f"Debes un total de {valor_cuenta}")
Total = 0

while True:
    try:

        ValorIngresado = int(input("Ingresa tu dinero: "))

        
        Total = ValorIngresado - valor_cuenta


        if Total <0:
            print(f"Su dinero no es duficiente intentelo de nuevo")
            print("Pago imediato")
            


        if Total >= 0:
            print(f"Su vuelto es de {Total}$")
            print("gracias por comprar!")

            break


        

    except ValueError:
        print("NO es dinero")
        print("Sea serio y pague")