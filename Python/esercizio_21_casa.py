maiuscola = lambda stringa :(stringa[0] >= 'A') & (stringa[0] <= 'Z')

stringa = input("Inserisci una stringa: ")

if maiuscola(stringa) == True:
    print("Inizia con una maisucola")
else:
    print("Non inizia con una maisucola")
