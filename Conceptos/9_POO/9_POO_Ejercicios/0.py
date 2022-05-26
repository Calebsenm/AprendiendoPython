
H = [

    [1,2],
    [3,4],
    [2,4],
    [5,5],
    [2,4],
    [1,2],
    [1,1]
]
h = []
for i in H:
    print(i)

for i in H:
    if i not in h:
        h.append(i)

for i in H:
    if i not in h:
        h.append(i)

print("Lista con eliminacion de duplicados")
for i in h:
    print(i)
