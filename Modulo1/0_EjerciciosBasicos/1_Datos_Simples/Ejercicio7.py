"""
Escribir un programa que pida 
al usuario su peso (en kg) y 
estatura (en metros), calcule
 el índice de masa corporal y lo
  almacene en una variable, y 
  muestre por pantalla la frase Tu índice
   de masa corporal es <imc> donde <imc> es 
   el índice de masa corporal calculado 
redondeado con dos decimales.

30 / 4 / 2022

"""
peso = int(input("ingresa tu peso en kilogramos>> "))
estatura = float(input("ingresa tu estatura en metros por ejemplo 1.60 >> "))

indice_corporal = (peso /(estatura **2)  )

print(f"tu indice de masa corporal es {indice_corporal}")
