from itertools import count


list = ['a','a','l','e','b']

list2 = ["0","0","0","0","0"]


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

a = indices(list, "a")
print(a)


for i in a:
    list2[i] = a


print("")
for i in list2:
    print(i)