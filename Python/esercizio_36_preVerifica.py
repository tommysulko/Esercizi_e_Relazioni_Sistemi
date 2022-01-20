import random

def spostamentoRandomFast():
    return random.choice([-1,1])

n = 0
listaSpostamento = [spostamentoRandomFast() for _ in range(5*24*60*60)] #giorni per ore per minuti per secondi

sommaMovimenti = 0
for movimenti in listaSpostamento:
    sommaMovimenti += movimenti
print(sommaMovimenti)
print 

