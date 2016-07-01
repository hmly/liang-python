# Liang 6.47
import turtle as t

def drawSQ(bColor, SQ_LENGTH):
    if bColor % 2 == 0: # Fill square with color, black
        t.begin_fill()
        
    for sq in range(4):
        t.pendown()
        t.forward(SQ_LENGTH)
        t.left(90)
        
    t.end_fill()

def drawChessboard(startx, endx, starty, endy):
    BOARD_ROW = BOARD_COLUMN = 8
    SQ_LENGTH = abs(endx - startx) // 8
    bColor = 1
    
    for i in range(BOARD_ROW):
        t.penup()
        bColor += 1
        t.goto(startx, starty - SQ_LENGTH * (i+1)) # Shift to next row
        for j in range(BOARD_COLUMN):
            drawSQ(bColor, SQ_LENGTH) 
            t.forward(SQ_LENGTH) # Shift to next column
            bColor += 1
                
def main():
    uInput = input('Enter two coordinates (start, end) x, y: ')
    startx, starty, endx, endy = [float(c) for c in uInput.split(',')]

    t.hideturtle()
    t.speed(0)
    
    drawChessboard(startx, endx, starty, endy) # 1st Checkboard
    startx = endx + (endx - startx) // 8 
    drawChessboard(startx, starty + startx, starty, endy) # 2nd Checkboard

    t.done()
    
if __name__ == '__main__':
    main()

# Ideal Test Inputs: -280, 280, 0, 0
                    # 200, -200, 10, 10
