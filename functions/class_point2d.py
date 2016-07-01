class Point2D:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        self.__norm = (x * x + y * y) ** (1/2)
        
    def getNorm(self):
        return self.__norm

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x
        self.__norm = (self.__x * self.__x + self.__y * self.__y) ** (1/2)

    def setY(self, y):
        self.__y = y
        self.__norm = (self.__x * self.__x + self.__y * self.__y) ** (1/2)

    
