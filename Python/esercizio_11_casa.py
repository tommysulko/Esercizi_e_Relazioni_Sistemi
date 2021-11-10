x1 = int(input("Inserisci la coordinata x del primo punto:"))
y1 = int(input("Inserisci la coordinata y del primo punto:"))
x2 = int(input("Inserisci la coordinata x del secondo punto:"))
y2 = int(input("Inserisci la coordinata y del secondo punto:"))
tupla = (x1,y1,x2,y2)

distanzaeculidea = ((x2**2 - x1**2) + (y2**2 - y1**2))*(1/2)

print(f"La distanza euclidea dei due punti è {distanzaeculidea} ")