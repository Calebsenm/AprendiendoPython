"""
Escribir un programa que pida al 
usuario un número entero y muestre 
por pantalla si es un número primo o no.

Finikitado 12/06/2022  6:40
"""


the_key_number = []
while True:
    the_number = int(input("put a number >> "))
    
    number_1 = 1
    while True:
        a =  the_number /number_1
        if a.is_integer() == True:
            the_key_number.append(True)
        if number_1 == the_number:
            break
        number_1 += 1
    
    print(the_key_number)
    if len(the_key_number) == 2:
        print(f"the number {the_number} is a Prime number")
        the_key_number.clear()
        
    else:
        print(f"the number {the_number} not  is a Prime number")
        the_key_number.clear()
      




