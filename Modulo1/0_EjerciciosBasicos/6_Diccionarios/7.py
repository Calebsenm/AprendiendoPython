# Ejercicio 7
# Escribir un programa que cree un 
# diccionario simulando una cesta 
# de la compra. El programa debe 
# preguntar el artículo y su precio 
# y añadir el par al diccionario,
#  hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla 
# la lista de la compra y el coste total,
#  con el siguiente formato


"""
ejemplo 
articulo1 = 200
....
total
"""
#easy 10/40
#18/06/2022



Compra = {}

while True:
    producto = input("Que producto deseas > ")
    valor = int(input(f"Cual es el precio de {producto} "))

    Compra[producto] = valor
    print()

    Total = 0
    for i in Compra:
        print(f"Articulo - {i}         precio - {Compra[i]}") 
        Total = Total + Compra[i]
    print("___________________________________") 
    print(f"                         Total {Total} $")   

    o = input("quieres salir si no > ")
    if o == "si":
        break
