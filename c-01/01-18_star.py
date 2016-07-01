# Liang 1.18

import turtle as t

def main():
    angles = [36, 144, 144, 144, 144]
    t.showturtle()
    
    for i in range(5):
        t.left(angles[i])
        t.forward(300)
        
    t.done()

main()
