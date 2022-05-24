from pickle import TRUE


hake = [True]
Hakemate = [False]

Hakemate.pop(0)
Hakemate.append(True)

if hake[0] == True:
    print("Hake")
if Hakemate[0] == True:
    print("Hakemate")