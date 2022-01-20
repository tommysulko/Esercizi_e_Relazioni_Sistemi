import turtle

griglia = turtle.Turtle()
y = 20
x = 0
for k in range (2):
    for i in range(5):
        griglia.forward(80)
        griglia.penup()
        griglia.goto(x,y)
        griglia.pendown()
        if k == 0:
            y = y + 20
        else:
            x = x + 20
    griglia.right(90)
    y = 80
    #incompleto