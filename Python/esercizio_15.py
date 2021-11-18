numeri = int(input("Inserisci il numero di numeri da inserire: "))
lista = []
risposta = "Si"

while(risposta == "Si"):
    num = float(input(f"Inserisci il numero della cella {cont}: "))
    lista.append(num)
    risposta = input("Vuoi inserire un altro numero? (Si o No)")
print(lista)
