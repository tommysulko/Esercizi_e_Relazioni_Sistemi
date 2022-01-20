from turtle import Turtle, Screen
import random

tartaruga = Turtle()
sfondo = Screen()
tartaruga.speed(30)

class stella():
    def __init__(self,coordX,coordY,dim):
        self.coordX = coordX
        self.coordY = coordY
        self.dim = dim
    
    def draw(self):
        tartaruga.penup()
        tartaruga.goto(self.coordX,self.coordY)
        tartaruga.pendown()
        count = 0
        angle = 144
        while count < 5:
            tartaruga.forward(self.dim)
            tartaruga.right(angle)
            count += 1
        #countRepeat += 1
        #if countRepeat >= 50:
            #return
        #else:
            #stella(countRepeat)


def main():
    for _ in range(50):
        stellax = stella(random.randint(-280,280),random.randint(-280,280),random.randint(10,30))
        stellax.draw()

if __name__ == "__main__":
    main()
