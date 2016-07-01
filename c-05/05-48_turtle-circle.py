# Liang 5.48
import turtle

NUM_OF_CIRCLE = 10
LENGTH_APART = 10

def drawCircle(numOfCircle):
    turtle.showturtle()
    turtle.speed(0)
    
    for i in range(1, numOfCircle + 1):
        turtle.circle(100 + i * LENGTH_APART)
        turtle.penup()
        turtle.goto(0, -i * LENGTH_APART)
        turtle.pendown()
        
    turtle.hideturtle()
    turtle.done()

def main():
    drawCircle(NUM_OF_CIRCLE)

main()
