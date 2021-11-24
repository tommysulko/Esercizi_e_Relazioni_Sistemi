maiuscola = lambda stringa :True if((stringa[0] >= 'A') & (stringa[0] <= 'Z'))else False

stringa = input("Inserisci una stringa: ")

if maiuscola(stringa) == True:
    print("Inizia con una maisucola")
else:
    print("Non inizia con una maisucola")