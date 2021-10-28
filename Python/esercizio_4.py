#slicing
stringa = "Classe quarta A robotica"
#le stringe in Python sono IMPUTABILI
#TypeError: 'str' object does not support item assignment

stringa_nuova = stringa[0:14] + 'B' + stringa[15:]
print(stringa_nuova)
print(f"LA STRINGA MODIFICATA E': {stringa_nuova}")

print(print) 




"""
print(f"Il primo carattere della stringa è {stringa[0]}")   #fstring
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

print(stringa[3:9]) #stampa la stringa dal primo indice al secondo indice escluso
print(stringa[0:6])

print(stringa[6:])  #dal 6 alla fine
print(stringa[:-2]) #stampa tutto fino al -2
print(stringa[2:14:2])  #prende tutti i caratteri dal 2 al 14 saltandone 2 
print(stringa[::-1])  #stampa la stringa al contrario. Inizo:fine:-1
"""
