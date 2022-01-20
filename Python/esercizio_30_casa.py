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

file = open("./primi.txt","w")
numPrimi=0
num=2

while(numPrimi<100):
    if(isPrimo(num)):
        file.write(str(num))
        numPrimi+=1
file.close()
