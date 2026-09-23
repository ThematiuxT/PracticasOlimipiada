lista = [5,6,7,5,6,7,9,0,10,6]
sum = 0
mayor = float('-inf')
menor = float('inf')
for n in lista:
    sum = sum + n
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
prom = sum/len(lista)
mprom = 0
for n in lista:
    if n > prom:
        mprom = mprom + 1
print(f"{prom} es el promedio, hay {mprom} números mayores")
print(f"{mayor} es el mas alto y {menor} el mas bajo")
