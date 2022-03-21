#. Realiza el código de 20 operaciones e imprime su resultado,
# usando los operadores de relación,
# aritméticos ,logicos y booleanos en un archivo con nombre operadores.py


#realiza  operaciones imprime el resultado  usando el operador  de relacion
# realiza  operaciones   imprimer el resultado usando los operadores aritmeticos
# realiza  operaciones imprime el resultado usando los operadores   booleanos
# realiza  operaciones imprime el resultado usando los operadores   booleanos

"""
operadores aritmeticos

+    es para sumar                    12+3 = 15
-    es para restar                   12-3 = 9
*    es para multiplicar              12*3 =  36
/    es para dividir                  12/3 = 4
%    es el modulo de las operaciones  12%3 = 1
**   es para realizar la potencia	    12**3 = 1728
//   realiza la division con el resultado de numero entero  18//5=3



operadores relacionales 

>   mayor que          12>3        True 
<   menor que          12<3        False 
==  esactamente igual  12 ==3      False
>=  mayor o igual      12 >=3      True
<=  menor o igual      12 <=3      False
!=  son diferentes     12 !=       True


operadores logicos 

and         Da True si los dos son True    2+1=3 and  3+2 =5     True
or          Da true si uno es verdadero    3+2=5  or  2-1 =5     True
not         da true si alguno de los operadores es falso    not 1+1==1  True


"""


print("Utilizo los operadores relacionales")

a = 1 >  2
print(f"1 > 2 {a}")


b = 3 < 5 
print(f"3 < 5 {b}")

c = 4==4 
print(f"4 == 4 {c}")


d = 2 <= 3
print(f"2 <=3 {d} ")


e = 2>=3 
print(f"2 >= 3 {e}")

f = 4!= 5
print(f"4!=5 {f}")

g =  5 !=5
print(f"5 != 5  {g}")


h = 5 == 4
print(f"5 == 4 {h}")


i =  6<6 
print(f"6 <6 {i}")

j = 7<= 7
print(f"7 <= 7 {j}")

"""

1 > 2 False
3 < 5 True
4 == 4 True
2 <=3 True 
2 >= 3 False
4!=5 True
5 != 5  False
5 == 4 False
6 <6 False
7 <= 7 True
"""
print("estos son los operadores aritmeticos")

a = 2 +2 
print(f" 2 + 2 = {a}")

a = 2 +3 
print(f" 2 + 2 = {a}")

a = 2 - 2 
print(f" 2 - 2 = {a}")

a = 2-1 
print(f" 2 - 1 = {a}")

a = 2 * 2 
print(f" 2 * 2 = {a}")

a = 2 * 3 
print(f" 2 * 3 = {a}")

a = 2 / 2 
print(f" 2 / 2 = {a}")

a = 2 /1 
print(f" 2 / 2 = {a}")


a = 5 % 2 
print(f" 5 % 2 = {a}")

a = 2 % 2 
print(f" 2 % 2 = {a}")

a = 2 ** 2 
print(f" 2 ** 2 = {a}")

a = 2 ** 3 
print(f" 2 **3 = {a}")

a = 2.2//2
print(f" 2.2 // 2 = {a}")


a = 10.2//3
print(f" 10.2 // 3 = {a}")



## ##################################
print("estos son los operadores logicos")


a = 3+1==4 and  4+4==8
print(f"3+1==4 and  4+4==8     ={a}")

##########################

a = 2 - 2 == 3 and 1+1==1
print(f"2 - 2 == 3 and 1+1==1  ={a}")


###########################
a = 2 - 2 == 3 or 1+1==1
print(f"2 - 2 == 3 or 1+1==1   ={a}")

##################

a = 2 + 2 == 4 or 1+1==1
print(f"2 + 2 == 4 or 1+1==1   ={a}")


##############################33

a = not 1+1==1
print(f" not 1+1==1            ={a}")
##############################
a = not 1+1==2
print(f" not 1+1==1            ={a}")