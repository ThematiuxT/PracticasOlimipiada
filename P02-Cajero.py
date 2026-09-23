print("Ingresa una cantidad de dinero")
monto = float(input())

denom = [500, 200, 100, 50, 20]
cant = {}
for d in denom:
    cant[d] = 0

while monto >= denom[-1]:
    for d in denom:
        if monto >= d:
            monto = monto - d
            cant[d] = cant[d] + 1
            break

for k, v in cant.items():
    if v > 0:
        print(f"{v} billetes de {k}")
print(f"{monto} restante")
