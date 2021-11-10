numero_1 = float(input("Inserisci il primo numero: "))
numero_2 = float(input("Inserisci il secondo numero: "))

quadrato_1 = numero_1 ** 2
quadrato_2 = numero_2 ** 2
somma = numero_1 + numero_2
differenza = quadrato_1 - quadrato_2
differenza_2 = (numero_1 - numero_2) ** 2

lista = [quadrato_1 + quadrato_2, somma**2, differenza, differenza_2]
print(lista)