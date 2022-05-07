""" 
ejercicio 7 Finikitado :D  2/03/2022

Escribir un programa que 
pregunte el correo electrónico 
del usuario en la consola y 
muestre por pantalla otro correo 
electrónico con el mismo nombre 
(la parte delante de la arroba 
@) pero con dominio ceu.es.

"""

correo_electronico = input("Ingresa tu correo electronico >> ")
email = "@ceu.es."

print(correo_electronico.replace("@gmail.com",email))

###la solucion correcta es 
email = input("Introduce tu correo electrónico: ")
#NO ENTIENDO QUE ES ESTO PERO HACE LO QUE LLO QUIERO
print(email[:email.find('@')] + '@ceu.es')



"""
Ingresa tu correo electronico >> hola@kdkjsf
hola@kdkjsf
Introduce tu correo electrónico: djids@djfidf
djids@ceu.es
"""