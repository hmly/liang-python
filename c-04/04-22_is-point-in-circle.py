# Liang 4.22
import math

def computeDistance(x1, y1, x2=0, y2=0):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def pointInCircle(x, y):
    if computeDistance(x, y) <= 10:
        return 'Point (%0.1f, %0.1f) is in the circle' % (x, y)
    else:
        return 'Point (%0.1f, %0.1f) is not in the circle' % (x, y)

def main():
    points = input('Enter a point (x, y): ')
    x, y = [float(p) for p in points.split(',')]
    print (pointInCircle(x, y))

main()
