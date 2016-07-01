# Liang 3.5

import math

def computePolyArea(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi/sides))

def main():
    sides = int(input('Enter the number of sides: '))
    lengths = float(input('Enter the side length: '))
    print('The area of the polygon is', computePolyArea(sides, lengths))

main()
