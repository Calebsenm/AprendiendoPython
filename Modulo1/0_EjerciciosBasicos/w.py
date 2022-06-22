# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")


# h = {"a":1,"b":2}

# if 1 in h:
#     print("Yes")

a = {1:{"itt":"True" ,"oll":11}, 2:{"itt":"False" ,"oll":11}}

for llave,key in a.items():
    if key["itt"] == "True":
        for llave2,key2 in key.items():
            print(llave2,":",key2)

