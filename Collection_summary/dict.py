Capitals = {"China": "Beijing",
           "India": "New Delhi",
           "USA": "Washington DC",
           "Russia": "Moscow"}


Copy_Capitals = Capitals.copy()
print(Copy_Capitals)
print(Capitals)

print("String=",str(Capitals))

for key in Capitals.keys():
    print(key)

for value in Capitals.values():
    print(value)

for i, j in Capitals.items():
    print(i,j)