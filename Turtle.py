import turtle
Dave = turtle.Turtle()
def moveFoward():
    Dave.forward(5)
def turnLeft():
    Dave.left(5)
def turnRight():
    Dave.right(5)
screen = turtle.Screen()
screen.onkey(moveFoward, "Up")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()
turtle.done()
