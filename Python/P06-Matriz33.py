matriz = [
    [5,6,8],
    [7,5,7],
    [6,7,2]
]

m_sum = 0
f_sums = [0,0,0]
c_sums = [0,0,0]
pd_sum = 0
sd_sum = 0
for fi, fil in enumerate(matriz):
    for ci, cel in enumerate(fil):
        m_sum = m_sum + cel
        f_sums[fi] = f_sums[fi] + cel
        c_sums[ci] = c_sums[ci] + cel
        if fi == ci:
            pd_sum = pd_sum + cel
        if fi == (2-ci):
            sd_sum = sd_sum + cel

print(f"Suma total: {m_sum}")
print(f"Sumas por fila:")
for suma in f_sums:
    print(suma)
print(f"Sumas por columna:")
for suma in c_sums:
    print(suma)
print(f"Suma diagonal principal: {pd_sum}")
print(f"Suma diagonal secundaria: {sd_sum}")
