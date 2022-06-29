# Ejercicio 4
# Escribir programa que 
# genere y muestre por pantalla 
# un DataFrame con los datos de 
# la tabla siguiente:


# Mes	Ventas	Gastos
# Enero	30500	22000
# Febrero	35600	23400
# Marzo	28300	18100
# Abril	33900	20700

import pandas as WAS

DATOS = {
    "MES":["Enero","Febrero","Marzo","Abril"],
    "VENTAS":[30500,35600,28300,33900],
    "GASTOS":[22000,23400,18100,20700]
}

Valores = WAS.DataFrame(DATOS)
print(Valores)