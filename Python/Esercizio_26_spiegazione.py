#modulo turtle
#Il modulo Turtle serve per disegnare attraverso Python
from turtle import Turtle, Screen

#tartaruga = Turtle()
#sfondo = Screen()
#tartaruga.forward(1000)

"""
Queste tre linee di codici servono per disegnare una riga attraverso python.
Cambiando il numero all'interno di foward() si può allungare la linea che si va a creare.
"""

"""
Se invece si vuole creare una curva bisogna scrivere il codice sottostante.
Con curva si intende un angolo retto in questo caso
"""
#tartaruga.right(100)
#tartaruga.forward(100)

"""
Grazie al modulo turtle si puà cambiare il colore di default della curva e dello sfondo.
Il colore della curva di default è nero mentre per lo sfondo il bianco
"""

#tartaruga = Turtle()
#sfondo = Screen()

#sfondo.colormode(255)

#R = 255
#G = 255
#B = 0

#sfondo.bgcolor((R, G, B))
#per cambiare il colore della curva invece si fa tartaruga.bgcolor((R, G, B))

"""
Con il modulo turtle si possono implementare i loop in modo da riuscire a stampare 
"""

#tartaruga = Turtle()

#for i in range(4):
#  tartaruga.forward(100)
#  tartaruga.right(90)

"""
Con questo loop creiamo una riga e cambiamo direzione verso destra di 90 gradi.
Dopo con il loop ricreriamo la stessa riga e ma verso una direzione diversa. Questo per un totale
di 4 volte creando un quadrato.
"""

tartaruga = Turtle()

for i in range(30):
    for i in range(4):
      tartaruga.forward(100)
      tartaruga.right(90)
    tartaruga.right(25)

"""

"""


"""
*
CODICE TROVATO PER CURIOSITA'
*

tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)

R = 255
G = 0
B = 0
sfondo.bgcolor((0, 0, 255))

tartaruga.speed(0)

colours = []

while G <= 255:
    colours.append((R, G, B))
    G += 1
while R >= 0:
    colours.append((R, G, B))
    R -= 1
while B < 255:
    colours.append((R, G, B))
    B += 1
while G > 0:
    colours.append((R, G, B))
    G -= 1
while R < 255:
    colours.append((R, G, B))
    R += 1

for i in range(3000):
  # La riga seguente fa cambiare di continuo il colore, anche se i è maggiore del numero di colori presenti nella lista
  tartaruga.color(colours[i % len(colours)])
  tartaruga.forward(i/3)
  tartaruga.right(119)
"""
