#Crea un programa que se llame Entrada.py, que permita leer correctamente los siguientes tipos de datos: entero, flotante, booleano, char, cadena.


a=int(1)
while True:
	print("si quieres salir ingresa x")
	dato = input("ingresa un dato: ")
	if dato == "x":
		break

	a=type(dato)
	print(f"El numero ingresado es: {a}")


