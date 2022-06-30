# Ejercicio 6
# Escribir una función que reciba un 
# dataframe de Pandas con los ingresos 
# y gastos de una empresa por meses y 
# devuelva un diagrama de líneas con dos 
# líneas, una para los ingresos y otra para 
# los gastos. El diagrama debe tener una leyenda 
# identificando la línea de los ingresos y la de 
# los gastos, un título con el nombre “Evolución 
# de ingresos y gastos” y el eje y debe empezar en 0.


# solo lo intenté crear y me dio flojara XD
# creo que no me gusta como tal la sciencia de datos 


# import matplotlib.pyplot as mp
# import pandas as pan
# def Funcion_data_frame(A):

#     fig, ax = mp.subplots()
#     ax.plot(A)
#     mp.title("ingresos")


#     return


# Datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
# Fram = pan.DataFrame(Datos)

# Funcion_data_frame(Fram)
# mp.show()



import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_lineas_ingresos_gastos(datos):
    fig, ax = plt.subplots()
    datos.plot(ax = ax)
    
    ax.set_ylim([0, max(datos.Ingresos.max(), datos.Gastos.max()) + 500])
    
    plt.title('Evolución de ingresos y gastos')
    return ax

datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
df_datos = pd.DataFrame(datos).set_index('Mes')
diagrama_lineas_ingresos_gastos(df_datos)
plt.show()