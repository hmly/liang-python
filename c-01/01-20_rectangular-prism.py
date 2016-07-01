# Liang 1.20

import turtle as t

def main():
    # Length, Width, Base Units(px)
    l = 300
    w = 150
    b = 50

    t.showturtle()
    
    # Front Rect
    t.goto(0, w)
    t.goto(l, w)
    t.goto(l, 0)
    t.goto(0, 0)

    # Back Rect
    t.goto(b, b)
    t.goto(l+b, b)
    t.goto(l+b, w+b)
    t.goto(b, w+b)

    # Edge 1-4
    t.goto(b, b)
    t.penup()
    t.goto(0, w)
    t.pendown()
    t.goto(b, w+b)
    t.penup()
    t.goto(l, w)
    t.pendown()
    t.goto(l+b, w+b)
    t.penup()
    t.goto(l, 0)
    t.pendown()
    t.goto(l+b, b)

    t.hideturtle()
    t.done()
    
main()
