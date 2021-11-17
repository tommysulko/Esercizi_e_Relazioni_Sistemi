numeri = int(input("Inserisci il numero di numeri da inserire: "))
lista = []
cont = 0

while(cont < numeri):
    num = float(input(f"Inserisci il numero della cella {cont}: "))
    lista.append(num)
    cont = cont + 1
print(lista)

max = lista[0]
min = lista[0]

for numeri in lista:
    if max > numeri:
        max = numeri
    
    if min <  numeri:
        min = numeri

print(f"Il massimo è {max}.")
print(f"Il minimo è {min}.")