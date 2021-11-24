maiuscola = lambda stringa :True if((stringa[0] >= 'A') & (stringa[0] <= 'Z'))else False
palindroma = lambda stringa:True if(stringa == stringa[::-1])else None

lista = ["Tommaso","CiiC","luca","porco"]
parolePalindrome = []
paroleMaiuscole = []


for parole in lista:
    if maiuscola(parole):
        paroleMaiuscole.append(parole)
    if palindroma(parole):
        parolePalindrome.append(parole)

print(f"Stringhe che iniziano per maiuscola {paroleMaiuscole}")
print(f"Stringhe palindrome {parolePalindrome}")