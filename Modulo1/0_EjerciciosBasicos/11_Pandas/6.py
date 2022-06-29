# Ejercicio 6
# El fichero cotizacion.csv contiene las cotizaciones 
# de las empresas del IBEX35 con las siguientes columnas: 
# nombre (nombre de la empresa), Final (precio de la acción 
# al cierre de bolsa), Máximo (precio máximo de la acción 
# durante la jornada), Mínimo (precio mínimo de la acción 
# durante la jornada), volumen (Volumen al cierre de bolsa),
#  Efectivo (capitalización al cierre en miles de euros). 
# Construir una función que construya un DataFrame a partir 
# del un fichero con el formato anterior y devuelva otro 
# DataFrame con el mínimo, el máximo y la media de dada 
# columna.

# import pandas as Pan

# def Funcion_data_Frame(Archive):

#     Diccionario = {}
#     Contenido = Archive.readlines()
#     Contenido2 = []
    
    
#     for i in Contenido:
#         A = i.split(";")
#         Contenido2.append(A)
    
#     Contenido3 = Contenido2[0]
#     # print(Contenido2)
#     Diccionario = {}
   
#     for i in Contenido2:
#         v = 0
#         for p in Contenido3:
#             A = []
            
#             for k in Contenido2:
                
#                 A.append(k[v])
#             v += 1
#             A.pop(0)
#             Diccionario[p] = A
              

  
#     Tabla = Pan.DataFrame(Diccionario)
#     return Tabla



# Archivo = open("11_Pandas/cotizacion.csv","r",encoding = "utf-8")

# Hola = Funcion_data_Frame(Archivo)

# print(Hola)
# Archivo.close()





import pandas as pd

def resumen_cotizaciones(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

AD = resumen_cotizaciones('11_Pandas/cotizacion.csv')
print(AD)