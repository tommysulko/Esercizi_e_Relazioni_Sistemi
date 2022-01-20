def PosizioneLettera(char):
    trovato = False
    posizione = 0
    while (trovato == False & posizione < 27):
        if(char == alfabeto[posizione]):
            trovato = True
        else:
            posizione +=1
    return (posizione)

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

scelta = (int(input("Inserisci 0 per codificare 1 per decodificare:")))
sliding = (int(input("Inserisci anche di quante lettere vuoi scorrere:")))
stringaCrittografata = ""
stringaDecri = ""
if scelta == 0:
    stringa = input("Inserisci la stringa che vuoi codificare:")
    stringa = stringa.upper()
    for lettera in stringa:
        letteraFin = PosizioneLettera(lettera) + sliding
        if letteraFin > (27-sliding):
            letteraFin = letteraFin % 27
        stringaCrittografata = stringaCrittografata + alfabeto[letteraFin]
    print(stringaCrittografata)
else:
    stringa = input("Inserisci la stringa che vuoi decodificare(TUTTO MAIUSCOLO):")
    for lettera in stringaCrittografata:
        letteraFin = PosizioneLettera(lettera) - sliding 
        if letteraFin < 0:
            letteraFin = letteraFin + alfabeto.__len__()
        stringaDecri = stringaDecri + alfabeto[letteraFin] 
    print(stringaDecri)