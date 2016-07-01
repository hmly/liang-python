import math


def area(r):
    return r * r * math.pi


def perimeter(r):
    return 2 * r * math.pi


radius = 5.5
print("area: %.3f" % area(radius))
print("perimeter: %.3f" % perimeter(radius))
