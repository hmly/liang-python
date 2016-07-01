import turtle as t

t.hideturtle()
t.speed(0)

def mousefunction(x, y):
    t.goto(x, y)
    t.write('%f, %f' % (x, y))

t.onscreenclick(mousefunction)
t.done()

def keyfunction():
    print ('Save the file')

t.onkey(keyfunction)
t.listen()
