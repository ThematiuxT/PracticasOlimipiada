matrizOG = [
    [1,2,3],
    [4,5,6],
]
transpuesta = []
for y, fila in enumerate(matrizOG):
    for x, celda in enumerate(fila):
        if y == 0:
            transpuesta.insert(x,[])
        transpuesta[x].insert(y,celda)

for fila in transpuesta:
    print(fila)
