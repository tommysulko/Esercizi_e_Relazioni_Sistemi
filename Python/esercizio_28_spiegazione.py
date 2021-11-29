#Uso dei file

f = open("./testo.txt","r")
righe = f.readline()
print(righe)
f.close()

f = open("./testo.txt","w")
f.write("Ciao")
f.close()