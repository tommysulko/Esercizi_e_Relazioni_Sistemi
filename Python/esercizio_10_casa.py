nome = input("Inserisci il tuo nome: ")

print(nome[0],end='')
for nome_nuovo in nome[1:]:
    print("*", end='')