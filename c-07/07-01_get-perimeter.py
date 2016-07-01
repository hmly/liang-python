# Liang 7.1

class Rectangle:

    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

def main():
    rectOne = Rectangle(4, 40)
    rectTwo = Rectangle(3.5, 35.7)

    for rect in [rectOne, rectTwo]:
        print ('%s \n width: %f \n height: %f \n area: %f \n perimeter: %f \n' % \
               ('Object: Rectangle', rect.width, rect.height, rect.getArea(), rect.getPerimeter()))

if __name__ == '__main__':
    main()
