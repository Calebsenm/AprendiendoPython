# Ejercicio 4
# Escribir un programa que acceda a 
# un fichero de internet mediante su 
# url y muestre por pantalla el número 
# de palabras que contiene.


def Funcion_ficheroWEB(Li):
    from urllib import request
    from urllib.error import URLError

    try:
        f = request.urlopen(Li)
    except URLError:
        return ("la url no existe")
    else:
        a = f.read()
        with open("pagina web.html","a") as F:
            
            F.write(str(a))

       
        return len(a)
  


link = "https://calebsenm.github.io/MyWeb.github.io/Prueba_ejercicioPython_ficherosN4.html"
print(Funcion_ficheroWEB(link))


