# Liang 6.18
from random import randint

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            if randint(0, 1):
                print (1, end=' ')
            else:
                print (0, end=' ')
        print ()

def main():
    num = int(input('Enter a number, n (for number of rows and columns): '))
    printMatrix(num)

if __name__ == '__main__':
    main()
