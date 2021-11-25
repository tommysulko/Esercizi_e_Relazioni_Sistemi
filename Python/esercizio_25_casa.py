pitagorica = [conta*numero for conta in range (11) for numero in range(11)]
indice1 = 0
indice2 = 11

for _ in range(11):
    print(pitagorica[indice1:indice2])
    indice1 += 11
    indice2 += 11 
