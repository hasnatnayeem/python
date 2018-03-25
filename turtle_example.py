import turtle


turtle.speed(1)
turtle.shape("turtle")

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

#drawSquare()
#drawTriangle()
drawDashedLine()
