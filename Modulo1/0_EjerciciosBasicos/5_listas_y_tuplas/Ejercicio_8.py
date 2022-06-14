"""
Escribir un programa 
que pida al usuario una 
palabra y muestre por 
pantalla si es un palíndromo.

#palíndromo.
It is a word that if you invert its writing it remains the same. example
Reconocer 


finished 13/06/2022   at 20:21 PM
"""

M = []
N = [] 

word =input("please input a word -> ")
for i in word:
    M.append(i)
    N.insert(0,i)

if M == N:
    print("is a palindrome ")
else:
    print("not is a palindrome")

