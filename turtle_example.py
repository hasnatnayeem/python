import turtle


turtle.speed(1)
turtle.shape("turtle")

def drawSquare():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.exitonclick()

def drawTriangle():
    turtle.speed(1)
    turtle.shape("turtle")

    turtle.left(60)
    turtle.forward(100)
    
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.exitonclick()

drawSquare()
#drawTriangle()
