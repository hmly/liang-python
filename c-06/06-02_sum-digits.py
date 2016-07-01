# Liang 6.2

def sumDigits(n):
    dSum = 0
    while n > 0:
        dSum += n % 10
        n //= 10
    return dSum

def main():
    num = int(input('Enter a number : '))
    print ('The sum of all the digits is %d' % sumDigits(num))

if __name__ == '__main__':
    main()
