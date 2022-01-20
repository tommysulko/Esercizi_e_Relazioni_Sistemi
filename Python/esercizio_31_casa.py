nome = input("Inserisci il tuo nome:")
cognome = input("Inserisci il tuo cognome:")
data = input("Inserisci la tua data di nascita (gg-mm-aa):")

dizionario = {"Nome":nome,"Cognome":cognome,"Data":data}
f= open("./anagrafico","w")



for chiave in dizionario: #dizionario = chiave:valore
    f.write(dizionario[chiave]+"\n")
    #f.write(f"{dizionario[chiave]}\n")
f.close()