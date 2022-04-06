#Realiza un programa que asigne un 
# valor entero usando un operador 
# ternario así: si 5>3 asigne 2, en 
# caso contrario asigne 4; luego, imprime
#  el resultado en la línea final. Guarda el 
# archivo como Ternario.py

#################################################################3
# EsAlto = True
# estado = "Bajo" if EsAlto else "Es bajo"
# print(estado)

# dato = 2 if  5>3 else 4
# print(dato)



edad = input("ingresa tu edad: ")
print("eres menor de edad" if int(edad) < 18 else "Eres mayor de edad") 



edad = int(input("ingresa tu edad: "))
if edad <18:
    print("eres menor edad")
else:
    print("eres mayor de edad")