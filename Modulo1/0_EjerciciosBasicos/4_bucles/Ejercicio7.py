"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
iterator1 =  1
iterator2 = 1


while True:
    #primer valor
    uno = iterator2
    #segundo valor
    dos = iterator1
    #resultado
    
    tres = uno*dos

    print(f"{uno}x{dos}={tres}")
    if iterator1 == 10:
        print()

        iterator1 = 0
        iterator2 += 1
    
    iterator1 += 1
    if iterator2 == 10:
        break
   
