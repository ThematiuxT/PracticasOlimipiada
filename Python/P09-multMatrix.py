matrizA = [
    [1,1],
    [2,2],
]

matrizB = [
    [1,2],
    [1,2],
]
def _getMatW(matriz: list[list[int]]) -> int:
    expected_width = len(matriz[0])
    for fila in matriz:
        if len(fila) != expected_width:   
            raise ValueError("Matrix is not rectangular")
    return expected_width

def multMatriz(matrizA, matrizB):
    if _getMatW(matrizA) != len(matrizB):
        raise ValueError("Dimensiones incorrectas para multiplicar")
    matriz_out = []
    for y, filaA in enumerate(matrizA):
        matriz_out.insert(y,[])
        for x, colB in enumerate(matrizB[y]):
            suma = 0
            for xA, A in enumerate(filaA):
                suma = suma + (filaA[xA] * matrizB[xA][x])
            matriz_out[y].insert(x,suma)

    return matriz_out
print( multMatriz(matrizA, matrizB) )
