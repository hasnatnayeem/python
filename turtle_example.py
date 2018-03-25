import turtle


turtle.speed(1)
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

#drawSquare()
#drawTriangle()
#drawDashedLine()
#drawMultipleSquare()
drawWheel()







