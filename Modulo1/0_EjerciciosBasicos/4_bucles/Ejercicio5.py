"""
Escribir un programa que pregunte al 
usuario una cantidad a invertir,
el interés anual y el número de años, 
y muestre por pantalla el capital obtenido 
en la inversión cada año que dura la inversión.

finikitado el 5:06 pm  10/06/2022
"""




cantidad = int(input("Ingrese la cantidad a invertir > "))
interes = int(input("Ingresa el interés > "))
anos = int(input("ingresa la cantidad de años > "))
print(f"La cantidad invertida es {cantidad} \nEl interés es {interes}\nAños a invertir {anos}")
    
iterator  = 0
while True:
    
    
    capital = ((cantidad * interes)/100)+cantidad
    cantidad = capital
    print(f"El capital obtenido en eñ año {iterator+1} es > {capital}")

    iterator += 1
    if iterator == anos:
        break