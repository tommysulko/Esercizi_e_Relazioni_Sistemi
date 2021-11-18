def isPrimo(num):
    contatore,divisore = 0,2
    primo = False
    while divisore<=(num*(1/2)) and contatore == 0:          
        if num%divisore == 0:
            contatore=+1
        divisore+=1
    
    if contatore == 0:
        primo = True
    else:
        primo = False
    return primo

#contatorePrimi = 0 
mille = 1000


primi = [k for k in range(2,1003) if isPrimo(k)]
print(f"Lista dei numeri primi: {primi}")

"""for numero in range(2,mille):
    isPrimo(numero)

    if isPrimo(numero) == True:
        contatorePrimi+=1
        primi.append(numero)
print(f"I numeri primi prima di 1000 sono {contatorePrimi}")
print(f"La lista dei numeri primi: {primi}")"""
