import turtle

NUMBER_OF_LICENSES = 10
ST_AVE = 5

def goodbyeMessage ():
    print ("Thank you for using the program!")
    
def reportFire ():
    print ("Reporting fire...")
    
def drawGrid ():
    turtle.showturtle()
    turtle.speed(0)
    print ("Drawing grid...")
    for i in range(ST_AVE):
        turtle.draw
    
def main ():
    drawGrid ()
    for i in range (NUMBER_OF_LICENSES):
        reportFire ()
    goodbyeMessage ()

if __name__ == "__main__":
    main()
