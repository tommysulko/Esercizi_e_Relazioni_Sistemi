from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()
f = open("./ScrivereComandiTurtle.txt",'r')
righe = f.readlines()

for r in righe:
    ls=r.split(":")


    print(ls)
    valore = ls[1]
    if(ls[0] == "speed"):
        tartaruga.speed(int(valore))
    if(ls[0] == "goto"):
        go = r.split(",")
        tartaruga.goto(int(go[1],go[1][:-1]))
    elif(ls[0] == "colormode"):
        sfondo.colormode(int(valore))
    elif(ls[0] == "bgcolor"): 
        color = r.split(",")
        sfondo.bgcolor(int(color[0],color[1][:-1]))
    elif(ls[0] == "color"):
        tartaruga.color(int(valore))
    elif(ls[0] == "right"):
        tartaruga.right(int(valore))
    elif(ls[0] == "left"):
        tartaruga.left(int(valore))    
    elif(ls[0] == "backward"):
        tartaruga.backward(int(valore))
    else:
        print("ERRORE")
sfondo.exitonclick()
f.close()

