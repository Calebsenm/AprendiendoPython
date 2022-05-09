"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas 
y no vegetarianas a sus clientes. Los ingredientes 
para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si 
quiere una pizza vegetariana o no, y en función 
de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir un 
ingrediente además de la mozzarella y el tomate que 
están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva.
"""

#finikitado el 9/05/2022   estubo interesante jajajaj casi una hora

Ingredientes_vege =["Pimiento","tofu"]
Ingredientes_novge=["Peperoni","Jamón","Salmón"]
Todos = ["Mozzarela","Tomate"]

tipo_pizza = input("Ingrese que tipo de pizza quiere >> Normal o Vejetariana  ")
if tipo_pizza.lower() == "normal":
    
    for i in range(len(Ingredientes_novge)):
        print(f"\n{i+1}.{Ingredientes_novge[i]}",end=" ")
        
    ingriente = int(input("\nIngrese el nuemro del ingrediente que desea ingrear "))

    if ingriente == 1:
        Todos.append(Ingredientes_novge[int(ingriente-1)])
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i+1}. {Todos[i]}",end=" ")
    elif ingriente == 2:
        Todos.append(Ingredientes_novge[int(ingriente-2)])
        
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i+1}. {Todos[i]}",end=" ")

    elif ingriente == 3:
        Todos.append(Ingredientes_novge[int(ingriente-3)])
       
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i+1}. {Todos[i]}",end=" ")

    


elif tipo_pizza.lower() == "vejetariana":
    for i in range(len(Ingredientes_vege)):
        print(f"\n{i+1} {Ingredientes_vege[i]}",end="")
       

    ingriente = int(input("\nIngrese el nuemro del ingrediente que desea ingresar "))
    if ingriente == 1:
        Todos.append(Ingredientes_vege[int(ingriente-1)])
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i}. {Todos[i]}",end=" ")
    elif ingriente == 2:
        Todos.append(Ingredientes_vege[int(ingriente-2)])
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i}. {Todos[i]}",end=" ")

    elif ingriente == 3:
        Todos.append(Ingredientes_vege[int(ingriente-3)])
        print(f"Ha elegido la pizaa {tipo_pizza}")
        for i in range(len(Todos)):
            print(f"\n{i}. {Todos[i]}",end=" ")
    else:
        print("Error")
    