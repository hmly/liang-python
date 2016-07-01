# Liang 3.19

import turtle

def drawLine(x1, y1, x2, y2):
    turtle.showturtle()
    turtle.penup()
    # Point 1
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.write((x1,y1), font=('Calibri', 8))
    # Point 2
    turtle.goto(x2, y2)
    turtle.write((x2,y2), font=('Calibri', 8))
    turtle.hideturtle()
    turtle.done()

def main():
    points = input('Enter two points(x,y): ')
    x1,y1,x2,y2 = [int(p) for p in points.split(',')]
    drawLine(x1,y1,x2,y2)

main()
