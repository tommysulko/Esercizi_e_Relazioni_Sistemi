maiuscola = lambda stringa :True if((stringa[0] >= 'A') & (stringa[0] <= 'Z'))else False
palindroma = lambda stringa:True if(stringa == stringa[::-1])else None

lista = ["Tommaso","CiiC","luca","porco"]
parolePalindrome = []
paroleMaiuscole = []

#paroleMaiuscole = [parola for parola in lista if maiuscola(parola)]
#parolePalindrome = [parola for parola in lista if palindroma(parola)]
#altro metodo

for parole in lista:
    if maiuscola(parole):
        paroleMaiuscole.append(parole)
    if palindroma(parole):
        parolePalindrome.append(parole)

print(f"Stringhe che iniziano per maiuscola {paroleMaiuscole}")
print(f"Stringhe palindrome {parolePalindrome}")
