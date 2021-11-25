palindroma = lambda stringa :(stringa == stringa[::-1])


stringa = input("Inserisci una stringa: ")

if palindroma(stringa) == True:
    print("la stringa è palindroma")
else:
    print("la stringa NON è palindroma")
