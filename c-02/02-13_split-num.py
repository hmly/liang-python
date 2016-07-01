# Liang 2.13

def splitNum(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits

def main():
    num = int(input('Enter an integer: '))
    revNum = splitNum(num)
    for i in range(0, -len(revNum), -1):
        print(revNum[i-1])
main()
