# Escribir un programa en el que se pregunte 
# al usuario por una frase y una letra, y muestre por 
# pantalla el número de veces que aparece la letra en la frase

# finished 12/06/2022  / 6:59
while True:
    phrase = input("please input a phrase >> ")
    word = input("please input a word >> ")
    
    counter1 = 0
    for i in phrase:
        if i == word:
            counter1 += 1
    
    print(f"The word is repeated {counter1} times ")

