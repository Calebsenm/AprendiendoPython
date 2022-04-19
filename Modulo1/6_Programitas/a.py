from itertools import count         


list1 = ['i','a','o','e','a']

list2 = ["0","0","0","0","0"]


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

a = indices(list1, "a")
print(a)

cuenta = len(a)
for i in range(cuenta):
    b = a[i]
    list2[b]= list1[b]

print("")
for i in list2:
    print(i)


# hola = "hola"
# hola2 = list("hola")

# print(hola2)