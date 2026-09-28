lista = [5,6,7,5,6,7,9,0,10,6]
output = []
for item in lista:
    if not item in output:
        output.append(item)

print(output)
