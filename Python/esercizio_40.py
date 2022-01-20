# 1. Chiedere stringa a utente
# 2. Ciclo su stringa in cui snobbate tutto cioò che non è parentesi
#()[]{}
# 3. Se trovo parentesi aperta faccio push
# 4. Se trovo parentesi chusa faccio pop
parentesiAperta = ["(","[","{"]
parentesiTutte = ["(",")","[","]","{","}"]
stringa = input("Inserisci una stringa:")
listaParentesi = []
inserimentoParentesiAperte = 0
inserimentoParentesiChiuse = 0
stringaNuova = ""

for carattere in stringa:
    stringaNuova = stringaNuova + carattere
    if carattere in parentesiTutte:
        
        if carattere in parentesiAperta:
            listaParentesi.append(carattere)
            inserimentoParentesiAperte += 1
        else:
            inserimentoParentesiChiuse += 1
            parentesi = listaParentesi.pop()
            if parentesi == '(' and carattere != ")":
                print("ERRORE DI PARENTESI CHIUSA")
                stringaNuova = stringaNuova[:-1] + ")"
            if parentesi == '[' and carattere != "]":
                print("ERRORE DI PARENTESI CHIUSA")
                stringaNuova = stringaNuova[:-1] + "]"
            if parentesi == '{' and carattere != "}":
                print("ERRORE DI PARENTESI CHIUSA")
                stringaNuova = stringaNuova[:-1] + "}"
if inserimentoParentesiAperte != inserimentoParentesiChiuse:
    print("Mancano alcune parentesi aperte o chiuse")
print(f"Stringa nuova corretta {stringaNuova}")