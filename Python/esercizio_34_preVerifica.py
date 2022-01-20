isVocale = lambda lettera: True if (lettera == 'A') | (lettera == 'E') | (lettera == 'I') | (lettera == 'O') | (lettera == 'U') | (lettera == 'a') | (lettera == 'e') | (lettera == 'i') | (lettera == 'o' )| (lettera == 'u') else False

risposta = input("Vuoi convertire una parola? (SI o NO):")
while(risposta == 'SI'):
    stringa = input("Inserisci una parola:")
    stringaNuova = ""
    for lettera in stringa:
        if isVocale(lettera):
            stringaNuova = stringaNuova + lettera
        else:
            stringaNuova = stringaNuova + lettera + 'o' + lettera
    print(stringaNuova)
    risposta = input("Vuoi inserire un'altra parola? (SI o NO):")