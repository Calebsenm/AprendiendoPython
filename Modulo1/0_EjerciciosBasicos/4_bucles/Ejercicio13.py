"""
Escribir un programa que muestre el eco de todo 
lo que el usuario introduzca hasta que el usuario 
escriba “salir” que terminará.

for example 
input  = 5
5
input


finished 12/06/2022 /7:11 Pm

"""

while True:
    hola = input("please input a phrase >> ")
    print(hola)

    if hola == "salir":
        break