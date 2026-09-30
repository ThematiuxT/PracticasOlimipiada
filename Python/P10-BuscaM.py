import math

tablero = [
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,1,1,0,0],
    [0,0,0,0,0],
]

rodear = []
for y in range(5):
    rodear.append([])
    for x in range(5):
        rodear[y].append(0)

for y, fila in enumerate(rodear):
    for x, celda in enumerate(fila):
        for dy in range(max(y-1,0),min(y+1,len(rodear)-1)+1):
            for dx in range(max(x-1,0),min(x+1,len(fila)-1)+1):
                if tablero[dy][dx] == 1 and not (dy == y and dx == x):
                    fila[x] = fila[x] + 1
print(rodear)
