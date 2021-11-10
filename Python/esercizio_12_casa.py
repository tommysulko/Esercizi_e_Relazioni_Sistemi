n1 = int(input("Inserisci il numero di volte che vuoi concatenare la stringa:"))
str =input("Inserisci la parola/frase:")

nuovastringa = ''

for contatore in range(n1):
    nuovastringa = nuovastringa + str

print(nuovastringa)