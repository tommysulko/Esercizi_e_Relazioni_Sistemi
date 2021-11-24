palindroma = lambda stringa :True if(stringa == stringa[::-1])else False


stringa = input("Inserisci una stringa: ")

if palindroma(stringa) == True:
    print("la stringa è palindroma")
else:
    print("la stringa NON è palindroma")