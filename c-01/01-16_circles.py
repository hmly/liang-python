# Liang 1.16

import turtle as t

def main():
    t.showturtle()
    pos = [[-45,0], [-45,-90], [45,0], [45,-90]]
    
    for i in range(4):
        t.penup()
        t.goto(pos[i])
        t.pendown()
        t.circle(45)
        
    t.done()

main()
