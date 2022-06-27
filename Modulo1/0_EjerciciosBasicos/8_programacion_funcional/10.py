
# Ejercicio 10
# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
# 
# La función recibirá como entrada la lista de inmuebles 
# y un precio, y devolverá otra lista con los inmuebles 
# cuyo precio sea menor o igual que el dado. Los inmuebles 
# de la lista que se devuelva deben incorporar un nuevo par 
# a cada diccionario con el precio del inmueble, donde el 
# precio de un inmueble se calcula con las siguiente fórmula 
# en función de la zona:

# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5


# Estubo bien cabron 
# fue bastante tiempo


{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 84000.0}, 
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 95000.0}


RealAstateList = [  
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

def real_estate_list(A,B):
    AB = []
    for i in A:
        if i["zona"] == "A":
            i["precio"] = (i["metros"] * 1000 + i["habitaciones"] * 5000 + int(i["garaje"]) * 15000) * (1- (2020-i["año"])/100)

        if i["zona"]  == "B":
            i["precio"] = (i["metros"] * 1000 + i["habitaciones"] * 5000 + int(i["garaje"]) * 15000) * (1- (2020-i["año"])/100) * 1.5
           
    for i in A:
        if  i["precio"] <= B :
            AB.append(i)

    return AB
print(real_estate_list(RealAstateList,100000))



