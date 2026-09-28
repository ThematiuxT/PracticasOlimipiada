print("Ingresa un numero entero positivo")
numero: int = int(input())
divisores: list[int] = []
for i in range(1, numero):
    if (numero % i) == 0:
        divisores.append(i)

sum_div = 0
for div in divisores:
    sum_div = div + sum_div

if sum_div == numero:
    print(f"{numero} es perfecto")
else:
    print(f"{numero} no es perfecto")
