# Torneo con fuerza F.
# Se seleccionan los dos mas chicos
# Costo de fusion = costo dos fuerzas
# Costo minimo total de todas las fusiones

#[4,3,2,7,6]
costo = 0
participantes = [4,3,2,7,6]

#un quicksort rapidito
def QuickSort(lista:list[int]) -> list[int]:
    if len(lista) <= 1:
        return lista
    p = lista[0]
    less = []
    more = []
    for item in lista[1::]:
        if item < p:
            less.append(item)
        else:
            more.append(item)

    less = QuickSort(less)
    more = QuickSort(more)
    final = []
    for item in less:
        final.append(item)
    final.append(p)
    for item in more:
        final.append(item)
    return final

while len(participantes)>1:
    participantes = QuickSort(participantes)
    costoInd = participantes[0] + participantes[1]
    costo = costo + costoInd
    participantes.pop(0)
    participantes[0] = costoInd

print(costo)
