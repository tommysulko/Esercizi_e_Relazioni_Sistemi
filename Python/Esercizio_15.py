numeri = int(input("Inserisci il numero di numeri da inserire: "))
lista = []
cont = 0

while(cont < numeri):
    num = float(input(f"Inserisci il numero della cella {cont}: "))
    lista.append(num)
    cont = cont + 1
print(lista)