"""
Escribir un programa 
que pregunte al usuario 
por el número de horas trabajadas 
y el coste por hora. Después debe
mostrar por pantalla la paga que 
le corresponde.


30 / 04 / 2022
"""

Horas_Trabajo = int(input("Porfavor ingrese las horas de trabajo que hace en un dia >> "))
Coste_Hora = int(input("Ingrese el coste por hora >> "))

print(f"El En el dia le corresponde {Horas_Trabajo * Coste_Hora}$")
Numeros_dias = int(input("Ingresa el nuemero de Dias >> "))
Ganancias_totales = Horas_Trabajo * Coste_Hora * Numeros_dias

print(f"En la semana le corresponde {Ganancias_totales}")

Ganancias_totales1 = Horas_Trabajo * Coste_Hora * 30
Ganancias_totales2 = Horas_Trabajo * Coste_Hora * 365

print(f"en un dia usted gana {Horas_Trabajo * Coste_Hora}")
print(f"En una semana usted gana {Ganancias_totales}")
print(f"En 30 dias usted  gana {Ganancias_totales1}")
print(f"En 365 dias usted gana {Ganancias_totales2}")