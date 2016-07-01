import turtle

class Shape:
    SIZE = 20
    def __init__ (self, x , y):
        self.x = x
        self.y = y
    def draw (self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.write("*")
        
class Circle (Shape):
    def __init__ (self, x, y):
        super().__init__(x, y)
    def draw (self):
        turtle.penup()
        turtle.goto(self.x, self.y - super().SIZE/2)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(super().SIZE)
