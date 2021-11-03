stringa = "Esercizio sulle stringhe"

print(f"Esercizio 1. Prima lettera:{stringa[0]}. Ultima lettera:{stringa[-1]}")
print(f"Esercizio 2. Stringa senza lettera iniziale e finale: {stringa[1:-1]}")
print(f"Esercizio 3. Stringa alternata di 1: {stringa[::1]}")
print(f"Esercizio 4. Stringa invertita di 1: {stringa[::-1]}")

stringa_nuova = stringa[0:2] + '?' + stringa[3:]
print(f"Esercizio 5. Carattere ? sostituita alla 3 lettera: {stringa_nuova}")