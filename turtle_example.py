import turtle
import random


turtle.speed(0)
turtle.shape("turtle")
turtle.color("Green")

def drawSquare():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.exitonclick()

def drawTriangle():
    turtle.left(60)
    turtle.forward(100)
    
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.exitonclick()

def drawDashedLine():
    for i in range(10):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    turtle.exitonclick()

def drawMultipleSquare():
    for side_length in range(50, 100, 10):
        for i in range(4):
            turtle.forward(side_length)
            turtle.left(90)
    turtle.exitonclick()

def drawWheel():
    turtle.speed(0)
    for k in range(36):
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(10)
    turtle.exitonclick()


def drawDots():
    height = 5
    width = 5
    step = 20
    turtle.penup()

    for i in range(height):
        for k in range(width):
            turtle.dot()
            turtle.forward(step)
        turtle.backward(width * step)
        turtle.right(90)
        turtle.forward(step)
        turtle.left(90)
    turtle.exitonclick()

def drawSquare(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def drawCircle():
    for i in range(90):
        drawSquare(90)
        turtle.right(4)
    turtle.exitonclick()

def drawRandomPoints():
    turtle.penup()
    for i in range(20):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.setposition(x, y)
        turtle.dot()
    turtle.exitonclick()
        

#drawSquare()
#drawTriangle()
#drawDashedLine()
#drawMultipleSquare()
#drawWheel()
#drawDots()
#drawCircle()

drawRandomPoints()



