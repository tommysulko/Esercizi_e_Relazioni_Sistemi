def Controllo(scelta,griglia):
    sbagliato = False
    if ((scelta < 0 & scelta > 8) & (griglia[scelta] != None)):
        sbagliato = True
    return sbagliato

griglia = {0:None,1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None}

print("GIOCO TRIS: PER TERMINARE IL GIOCO FARE LA COMBINAZIONE Ctrl+C")
partitaFinita = False
while(True):

    giocatore1 = int(input("Giocatore 1 inserisci la cella dove vuoi mettere la X ( tra 0 e 8 e non già occupata ):"))
    while(Controllo(giocatore1,griglia)):
        giocatore1 = int(input("Giocatore 1 inserisci la cella dove vuoi mettere la X ( tra 0 e 8 e non già occupata ):"))
    griglia[giocatore1] = 'X'

    giocatore2 = int(input("Giocatore 2 inserisci la cella dove vuoi mettere la X ( tra 0 e 8 e non già occupata ):"))
    while(Controllo(giocatore2,griglia)):
        giocatore1 = int(input("Giocatore 2 inserisci la cella dove vuoi mettere la X ( tra 0 e 8 e non già occupata ):"))
    griglia[giocatore2] = 'O'
    
    #disegno griglia
    
    print(griglia)


"""
O | X | X
----------
O | O | O
----------
X | O | O 
"""