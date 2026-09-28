matrizA = [
    [1,0],
    [0,1],
]

matrizB = [
    [5,4],
    [2,3],
]

def _getMatW(matriz: list[list[int]]):
    expected_width = len(matriz[0])
    for fila in matriz:
        if len(fila) != expected_width:   
            raise ValueError("Matrix is not rectangular")
    return expected_width

def sumarMatriz(matrizA, matrizB):
    a_height = len(matrizA)
    b_height = len(matrizB)

    if a_height != b_height:
        raise ValueError("Matrix sizes dont match")

    width = _getMatW(matrizA)
    if _getMatW(matrizB) != width:
        raise ValueError("Matrix sizes dont match")

    matrizOut = []

    for y in range(a_height):
        matrizOut.insert(y,[])
        for x in range(width):
            matrizOut[y].insert(x,matrizA[y][x] + matrizB[y][x])
    return matrizOut

print(sumarMatriz(matrizA,matrizB))
            

