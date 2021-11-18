numeri = int(input("Inserisci il numero di numeri da inserire: "))
lista = []
risposta = "Si"

while(risposta == "Si"):
    num = int(input(f"Inserisci un nuovo numero: "))
    lista.append(num)
    risposta = input("Vuoi inserire un altro numero? (Si o No)")
print(lista)
