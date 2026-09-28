lista = [4, 9, 2, 9, 7, 5]
big = lista[0]
sbig = float("-inf")
for item in lista:
    if big < item:
        big = item
    if sbig < item < big:
        sbig = item
print(sbig)
