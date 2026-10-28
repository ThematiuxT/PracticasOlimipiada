"""Calle circular robar casas
cada c tiene dinero, no se pueden robar casas adjacentes
5 [2,7,9,3,1]"""
calle = [2,7,9,3,1]
cont = True
dinero_robado = 0 
while cont:
    calleT = []
    for n,casa in enumerate(calle):
        #Valor real = valor - valor vecinos
        calleT.append(casa-(calle[n-1]+calle[(n+1)%len(calle)]))
        best_pos = 0
    for n,casa in enumerate(calleT):
        #Tomar casa con mejor valor total.
        #O mejor ganancia directa si T es 0
        if casa > calleT[best_pos] or (calleT[best_pos] == 0 and calle[n]>0):
            best_pos = n
    dinero_robado = dinero_robado + calle[best_pos]
    print(f"Robar casa {best_pos} for {calle[best_pos]}")
    for n in [-1,0,1]:
        calle[(best_pos+n)%len(calle)] = 0
    cont = False
    for casa in calle:
        cont = cont or casa != 0

print(f"Total ganado:{dinero_robado}")
