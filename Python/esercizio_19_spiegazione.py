dispari = [k for k in range(2,1003) if k%2 != 0]
print(f"Lista Dispari: {dispari}")

#comprensione di liste

nomi = ["marco","luca","mario","valeria","maria"]

nomi_m = [nome for nome in nomi if nome[0] == 'm']
print(f"Nomi che iniziano con M: {nomi_m}")

#------------------------Funzioni------------------------

def nomefunzione(parametri):
    #codice
    #return variabile (ci può essere e non essere)
    #effetti collaterali
    print()

def somma_moltiplicazione(x,y):
    somma = x+y
    moltiplicazione = x*y
    #return somma,moltiplicazione
    return {"somma":somma, "moltiplicazione":moltiplicazione}

a=10
b=4

#s, m = somma_moltiplicazione(a,b)
print(somma_moltiplicazione(a,b))

#lambda function

somma_moltiplicazione = lambda x,y : (x+y,x*y)

"""
moduli python = librerie e possono essere nativi, moduli già presenti nell'instal. di 
python e poi
quelli non nativi da installare
"""